import aiohttp
import json
from hashlib import sha256
import base64

import logging

from typing import Optional

from .websocket_client import WebSocketClient
from libwsctrl.protocols.obs_ws4.obs_websocket_protocol import *
from ..structs.callback import Callback


class OBSWebsocketClient (WebSocketClient):

    def __init__(self, address: str, timeout: float=300):
        super().__init__(address, timeout)

        self.callbacks = {}
        self.eventListeners = {}
        self.authenticated = False

    async def connect(self, password: Optional[str] = None, onAuthenticated: Callback = None):
        await super().connect()
        self.sendMessageJson(getAuthRequired(), Callback(self.authenticate, password=password, onAuthenticated=onAuthenticated))

    def authenticate (self, msg, password=None, onAuthenticated=None):
        if msg['authRequired'] == False:
            self.authenticated = True
            onAuthenticated.putArgument('msg', {'status': msg['status']})
            onAuthenticated.call()
            return
        if password is None:
            return

        secret = sha256()
        secret.update(password.encode("utf-8"))
        secret.update(msg['salt'].encode("utf-8"))

        secret64 = base64.b64encode(secret.digest())

        response = sha256()
        response.update(secret64)
        response.update(msg['challenge'].encode("utf-8"))
        response64 = base64.b64encode(response.digest()).decode("utf-8")

        self.sendMessageJson(authenticate(response64), onAuthenticated)

    def sendMessageJson(self, data: Any, callback: Callback=None):
        if callback is not None:
           self.addCallback(data["message-id"], callback)
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
        cb : Callback = self.callbacks[jsn["message-id"]]
        del self.callbacks[jsn["message-id"]]
        cb.putArgument("msg", jsn)
        try:
            cb.call()
        except Exception as ex:
            logging.exception(ex)

    def executeEventListener(self, jsn):
        events = self.eventListeners[jsn['update-type']]
        for e in events:
            e.putArgument("msg", jsn)
            try:
                e.call()
            except Exception as ex:
                logging.exception(ex)

    async def processAnswer(self, msg):
        if msg.type == aiohttp.WSMsgType.TEXT:
            jsn = json.loads(msg.data)
            if "message-id" in jsn and jsn["message-id"] in self.callbacks:
                try:
                    self.executeCallback(jsn)
                except Exception as ex:
                    logging.exception(ex)
            elif "update-type" in jsn and jsn['update-type'] in self.eventListeners:
                try:
                    self.executeEventListener(jsn)
                except Exception as ex:
                    logging.exception(ex)
