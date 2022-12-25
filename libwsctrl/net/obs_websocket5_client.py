from typing import Callable

import aiohttp
import json
from hashlib import sha256
import base64

import logging

from .websocket_client import WebSocketClient
from libwsctrl.protocols.obs_ws5.requests import *
from ..protocols.obs_ws5.enums import WebSocketOpCode, EventSubscription
from ..structs.callback import Callback


class OBSWebsocketClient (WebSocketClient):

    def __init__(self, address: str, timeout: float=300):
        super().__init__(address, timeout)

        self.callbacks = {}
        self.eventListeners = {}
        self.REQUEST_HANDLERS: Dict[int, Callable[[Dict[str, Any]], None]] = {
            WebSocketOpCode.Hello.value: self.onOpHello,
            WebSocketOpCode.Identify.value: self.onOpIdentify,
            WebSocketOpCode.Identified.value: self.onOpIdentified,
            WebSocketOpCode.Reidentify.value: self.onOpReidentify,
            WebSocketOpCode.Event.value: self.onOpEvent,
            WebSocketOpCode.Request.value: self.onOpRequest,
            WebSocketOpCode.RequestResponse.value: self.onOpRequestResponse,
            WebSocketOpCode.RequestBatch.value: self.onOpRequestBatch,
            WebSocketOpCode.RequestBatchResponse.value: self.onOpRequestBatchResponse
        }
        self.password = None
        self.onAuthenticated = None
        self.authenticated = False

    def __createMessage(self, opcode: int, data=None) -> dict:
        """
        :param requestType: Request Type
        :param data: Additional data fields for the request
        :return: A dictionary containing all message fields
        """
        result = {}

        if data is None:
            data = {}

        result["op"] = opcode
        result["d"] = data

        return result

    async def connect(self, password: Optional[str] = None, onAuthenticated: Callback = None):
        self.password = password
        self.onAuthenticated = onAuthenticated
        await super().connect({"Sec-WebSocket-Protocol": "obswebsocket.json"})

    def authenticate (self, msg, password=None):
        if password is None:
            return

        secret = sha256()
        secret.update(password.encode("utf-8"))
        secret.update(msg['authentication']['salt'].encode("utf-8"))

        secret64 = base64.b64encode(secret.digest())

        response = sha256()
        response.update(secret64)
        response.update(msg['authentication']['challenge'].encode("utf-8"))
        response64 = base64.b64encode(response.digest()).decode("utf-8")

        message = self.__createMessage(1, {
            "rpcVersion": 1,
            "authentication": response64,
            "eventSubscriptions": EventSubscription.All.value
        })

        self.sendMessageJson(message)

    def sendMessageJson(self, data: Any, callback: Callback=None):
        if data["op"] == 6 and callback is not None:
           self.addCallback(data["d"]["requestId"], callback)
        return super().sendMessageJson(data)

    def addEventListener(self, event, listener):
        if not event in self.eventListeners:
            self.eventListeners[event] = []
        self.eventListeners[event].append(listener)

    def removeEventListener (self, event, listener):
        if event not in self.eventListeners or listener not in self.eventListeners[event]:
            return None
        return self.eventListeners[event].remove(listener)

    def addCallback (self, name, callback):
        if name not in self.callbacks:
            self.callbacks[name] = callback

    def executeCallback(self, jsn):
        cb : Callback = self.callbacks[jsn["d"]["requestId"]]
        del self.callbacks[jsn["d"]["requestId"]]
        cb.putArgument("msg", jsn)
        try:
            cb.call()
        except Exception as ex:
            logging.exception(ex)

    def executeEventListener(self, jsn):
        events = self.eventListeners[jsn['d']['eventType']]
        for e in events:
            e.putArgument("msg", jsn)
            try:
                e.call()
            except Exception as ex:
                logging.exception(ex)

    def onOpHello(self, msg: Dict[str, Any]):
        """
        First message sent from the server immediately on client connection.
        Contains authentication information if auth is required.
        Also contains RPC version for version negotiation.

        :param msg: Parsed message
        :return: None
        """
        data: dict = msg["d"]
        if 'authentication' in data.keys():
            self.authenticate(data, self.password)

    def onOpIdentify(self, msg: Dict[str, Any]):
        # Not Implemented, Outgoing only
        pass

    def onOpIdentified(self, msg: Dict[str, Any]):
        self.onAuthenticated.putArgument('msg', msg)
        self.onAuthenticated.call()
        pass

    def onOpReidentify(self, msg: Dict[str, Any]):
        # Not Implemented, Outgoing only
        pass

    def onOpEvent(self, msg: Dict[str, Any]):
        if msg['d']['eventType'] in self.eventListeners:
            try:
                self.executeEventListener(msg)
            except Exception as ex:
                logging.exception(ex)

    def onOpRequest(self, msg: Dict[str, Any]):
        # Not Implemented, Outgoing only
        pass

    def onOpRequestResponse(self, msg: Dict[str, Any]):
        if msg["d"]["requestId"] in self.callbacks:
            try:
                self.executeCallback(msg)
            except Exception as ex:
                logging.exception(ex)

    def onOpRequestBatch(self, msg: Dict[str, Any]):
        pass

    def onOpRequestBatchResponse(self, msg: Dict[str, Any]):
        pass

    async def processAnswer(self, msg):
        if msg.type == aiohttp.WSMsgType.TEXT:
            jsn = json.loads(msg.data)
            try:
                self.REQUEST_HANDLERS[jsn['op']](jsn)
            except Exception as ex:
                logging.exception(ex)
