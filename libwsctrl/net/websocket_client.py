from asyncio import sleep
from typing import Any

import aiohttp
from asyncio.queues import Queue, QueueEmpty

from virtualstudio.common.logging import logengine


class WebSocketClient:

    def __init__(self, address: str, timeout: float=300):
        super().__init__()
        self._address = address
        self._timeout = timeout

        self.session = None
        self.ws = None

        self.sendQueue = Queue()
        self.logger = logengine.getLogger()

        self.shouldClose = False

    async def connect(self):
        self.shouldClose = False
        self.session = aiohttp.ClientSession()
        self.ws = await self.session.ws_connect(url=self._address, timeout=self._timeout)

    def requestClose(self):
        self.shouldClose = True

    async def close(self):
        await self.session.close()

    def isConnected(self):
        return self.ws is not None and not self.session.closed

    async def recieveLoop(self):
        async for msg in self.ws:
            await self.processAnswer(msg)

    async def sendLoop(self):
        while not self.shouldClose:
            try:
                request = self.sendQueue.get_nowait()
            except QueueEmpty:
                await sleep(0.001)
                continue

            if isinstance(request, str):
                await self.ws.send_str(request)
            elif isinstance(request, (bytes, bytearray, memoryview)):
                await self.ws.send_bytes(request)
            else:
                await self.ws.send_json(request)
        await self.close()

    def sendMessageJson(self, data: Any):
        self.sendQueue.put_nowait(data)

    def sendMessageStr(self, data: str):
        self.sendQueue.put_nowait(data)

    def sendMessageBytes(self, data):
        self.sendQueue.put_nowait(data)

    async def processAnswer(self, msg):
        pass
