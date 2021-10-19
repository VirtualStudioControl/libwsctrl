from typing import Any, Optional, Dict

__MESSAGE_ID = 0

Object = Dict[str, Any]

def getMessageID() -> str:
    global __MESSAGE_ID
    ret = "PY_WSCTRL-" + hex(__MESSAGE_ID)
    __MESSAGE_ID = __MESSAGE_ID+1
    return ret


def __createJSON(request: str, params=None) -> dict:
    if params is None:
        params = {}
    params["request-type"] = request
    params["message-id"] = getMessageID()
    return params


#region General

def getVersion() -> dict:
    return __createJSON("GetVersion")


def getAuthRequired() -> dict:
    return __createJSON("GetAuthRequired")


def authenticate(auth: str) -> dict:
    return __createJSON("Authenticate", {'auth': auth})


def setFilenameFormatting(formatting: str) -> dict:
    return __createJSON("SetFilenameFormatting", {'filename-formatting': formatting})


def getFilenameFormatting() -> dict:
    return __createJSON("GetFilenameFormatting", {})


def getStats() -> dict:
    return __createJSON("GetStats", {})


def broadcastCustomMessage(realm: str, data: Any) -> dict:
    return __createJSON("BroadcastCustomMessage", {'realm': realm, 'data': data})


def getVideoInfo() -> dict:
    return __createJSON("GetVideoInfo", {})


def openProjector(type: Optional[str] = None, monitor: Optional[int] = None, geometry: Optional[str] = None,
                  name: Optional[str] = None) -> dict:
    obj = {}
    if type is not None:
        obj["type"] = type

    if monitor is not None:
        obj["monitor"] = monitor

    if geometry is not None:
        obj["geometry"] = geometry

    if name is not None:
        obj["name"] = name

    return __createJSON("OpenProjector", obj)


def triggerHotkeyByName(hotkeyName : str) -> dict:
    return __createJSON("GetVideoInfo", {"hotkeyName": hotkeyName})


def triggerHotkeyBySequence(keyId: str, shift: bool = False, alt: bool = False, control: bool = False,
                            command: bool = False) -> dict:
    mods = {}
    if shift:
        mods["shift"] = shift

    if alt:
        mods["alt"] = alt

    if control:
        mods["control"] = control

    if command:
        mods["command"] = command

    return __createJSON("OpenProjector", {"keyId" : keyId, "keyModifiers": mods})

def executeBatch(*requests : any, abortOnFail: Optional[bool] = None) -> dict:
    params = {"requests": requests}

    if abortOnFail is not None:
        params['abortOnFail'] = abortOnFail

    return __createJSON("ExecuteBatch", params)

def sleep(sleepMillis : int):
    return __createJSON("Sleep", {'sleepMillis': sleepMillis})

#endregion


#region Media Control

def playPauseMedia(sourceName: str, pause: Optional[bool] = None):
    params = {'sourceName': sourceName}

    if pause is not None:
        params['pause'] = pause

    return __createJSON("PlayPauseMedia", params)


def restartMedia(sourceName: str):
    return __createJSON("RestartMedia", {'sourceName': sourceName})


def stopMedia(sourceName: str):
    return __createJSON("StopMedia", {'sourceName': sourceName})


def nextMedia(sourceName: str):
    return __createJSON("NextMedia", {'sourceName': sourceName})


def previousMedia(sourceName: str):
    return __createJSON("PreviousMedia", {'sourceName': sourceName})


def getMediaDuration(sourceName: str):
    return __createJSON("GetMediaDuration", {'sourceName': sourceName})


def getMediaTime(sourceName: str):
    return __createJSON("GetMediaTime", {'sourceName': sourceName})


def setMediaTime(sourceName: str, timestamp: int):
    return __createJSON("SetMediaTime", {'sourceName': sourceName, 'timestamp': timestamp})


def scrubMedia(sourceName: str, timeOffset: int):
    return __createJSON("ScrubMedia", {'sourceName': sourceName, 'timeOffset': timeOffset})


def getMediaState(sourceName: str):
    return __createJSON("GetMediaState", {'sourceName': sourceName})

#endregion

#region Sources

def getMediaSourcesList():
    return __createJSON("GetMediaSourcesList", {})


def createSource(sourceName: str, sourceKind: str, sceneName: str, sourceSettings: Object = None, setVisible: bool = True):
    if sourceSettings is None:
        sourceSettings = {}
    return __createJSON("CreateSource", {'sourceName': sourceName,
                                         'sourceKind': sourceKind,
                                         'sceneName': sceneName,
                                         'sourceSettings': sourceSettings,
                                         'setVisible': setVisible})


def getSourcesList():
    return __createJSON("GetSourcesList", {})


def getSourceTypesList():
    return __createJSON("GetSourceTypesList", {})


def getVolume(source: str, useDecibel: bool = False):
    return __createJSON("GetVolume", {'source': source, 'useDecibel': useDecibel})


def setVolume(source: str, volume: float, useDecibel: bool = False):
    return __createJSON("GetVolume", {'source': source, 'volume': volume, 'useDecibel': useDecibel})


def setAudioTracks(sourceName: str, track: int, active: bool):
    return __createJSON("GetVolume", {'sourceName': sourceName, 'track': track, 'active': active})


def getAudioTracks(sourceName: str):
    return __createJSON("GetAudioTracks", {'sourceName': sourceName})


def getMute(source: str):
    return __createJSON("GetMute", {'source': source})


def setMute(source: str, mute: bool):
    return __createJSON("SetMute", {'source': source, 'mute': mute})


def toggleMute(source: str):
    return __createJSON("ToggleMute", {'source': source})


def getSourceActive(sourceName: str):
    return __createJSON("GetSourceActive", {'sourceName': sourceName})


def getAudioActive(sourceName: str):
    return __createJSON("getAudioActive", {'sourceName': sourceName})



#endregion