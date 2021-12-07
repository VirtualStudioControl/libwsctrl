from libwsctrl.net.obs_websocket4_client import OBSWebsocketClient
from libwsctrl.protocols.obs_ws4.obs_websocket_protocol import *
from libwsctrl.protocols.obs_ws4.obs_websocket_events import *

import asyncio

from libwsctrl.structs.callback import Callback


wsClient: OBSWebsocketClient = None


def printAll(*args, **kwargs):
    print("ARGS:", args)
    print("KWAS:", kwargs)

def onAuthenticated(msg):
    callback = Callback(printAll)
    wsClient.addEventListener(event=EVENT_SCENEITEMVISIBILITYCHANGED, listener=callback)
    wsClient.sendMessageJson(getSceneList(), callback=callback)



async def main():
    global wsClient
    wsClient = OBSWebsocketClient("ws://127.0.0.1:4444") #"ws://192.168.114.230:4444"
    await wsClient.connect(password="12345678", onAuthenticated=Callback(onAuthenticated))
    rcvLoop = wsClient.recieveLoop()
    sendLoop = wsClient.sendLoop()

    await asyncio.gather(rcvLoop, sendLoop, return_exceptions=True)

if __name__ == "__main__":
    asyncio.run(main())
