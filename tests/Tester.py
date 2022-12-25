from libwsctrl.net.obs_websocket5_client import OBSWebsocketClient
from libwsctrl.protocols.obs_ws5.requests import *
from libwsctrl.protocols.obs_ws5.events import EVENT_SCENEITEMENABLESTATECHANGED

import asyncio

from libwsctrl.structs.callback import Callback


wsClient: OBSWebsocketClient = None


def printAll(*args, **kwargs):
    print("ARGS:", args)
    print("KWAS:", kwargs)

def onAuthenticated(msg):
    callback = Callback(printAll)
    wsClient.addEventListener(event=EVENT_SCENEITEMENABLESTATECHANGED, listener=callback)
    wsClient.sendMessageJson(getSourceFilterList("Notes"), callback=callback)


async def main():
    global wsClient
    wsClient = OBSWebsocketClient("ws://192.168.0.94:4455") #"ws://192.168.114.230:4444"
    await wsClient.connect(password="W3GRyd13y1cXw4aD", onAuthenticated=Callback(onAuthenticated))
    rcvLoop = wsClient.recieveLoop()
    sendLoop = wsClient.sendLoop()

    await asyncio.gather(rcvLoop, sendLoop, return_exceptions=True)

if __name__ == "__main__":
    asyncio.run(main())
