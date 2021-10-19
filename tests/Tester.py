from libwsctrl.net.obs_websocket4_client import OBSWebsocketClient
from libwsctrl.protocols.obs_ws4.obs_websocket_protocol import *

import asyncio

async def main():
    wsClient = OBSWebsocketClient("ws://127.0.0.1:4444")
    await wsClient.connect(password="12345678")
    rcvLoop = wsClient.recieveLoop()
    sendLoop = wsClient.sendLoop()

    wsClient.sendMessageJson(getVersion())

    await asyncio.gather(rcvLoop, sendLoop, return_exceptions=True)

if __name__ == "__main__":
    asyncio.run(main())
