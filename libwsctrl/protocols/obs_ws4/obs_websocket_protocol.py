from copy import deepcopy
from typing import Any, Dict, List, Union

__MESSAGE_ID = 0

Object = Dict[str, Any]


def getMessageID() -> str:
    global __MESSAGE_ID
    ret = "PY_WSCTRL-" + hex(__MESSAGE_ID)
    __MESSAGE_ID = __MESSAGE_ID + 1
    return ret


def __createJSON(request: str, params=None) -> dict:
    if params is None:
        params = {}
    params["request-type"] = request
    params["message-id"] = getMessageID()
    return params


# region GENERAL
def getVersion():
    """
    Returns the latest version of the plugin and the API.
    """
    return __createJSON("GetVersion", {})


def getAuthRequired():
    """
    Tells the client if authentication is required. If so, returns authentication parameters `challenge`
    and `salt` (see "Authentication" for more information).
    """
    return __createJSON("GetAuthRequired", {})


def authenticate(auth: str):
    """
    Attempt to authenticate the client to the server.

    :param auth: String - Response to the auth challenge (see "Authentication" for more information).
    """
    return __createJSON("Authenticate", {'auth': auth})


def setHeartbeat(enable: bool):
    """
    Enable/disable sending of the Heartbeat event

        :param enable: boolean - Starts/Stops emitting heartbeat messages

    """
    return __createJSON("SetHeartbeat", {'enable': enable})


def setFilenameFormatting(filename_formatting: str):
    """
    Set the filename formatting string

        :param filename_formatting: String - Filename formatting string to set.

    """
    return __createJSON("SetFilenameFormatting", {'filename-formatting': filename_formatting})


def getFilenameFormatting():
    """
    Get the filename formatting string


    """
    return __createJSON("GetFilenameFormatting", {})


def getStats():
    """
    Get OBS stats (almost the same info as provided in OBS' stats window)


    """
    return __createJSON("GetStats", {})


def broadcastCustomMessage(realm: str, data: Object):
    """
    Broadcast custom message to all connected WebSocket clients

        :param realm: String - Identifier to be choosen by the client
        :param data: Object - User-defined data

    """
    return __createJSON("BroadcastCustomMessage", {'realm': realm, 'data': data})


def getVideoInfo():
    """
    Get basic OBS video information


    """
    return __createJSON("GetVideoInfo", {})


def openProjector(type: str = '', monitor: int = 0, geometry: str = '', name: str = ''):
    """
    Open a projector window or create a projector on a monitor. Requires OBS v24.0.4 or newer.

        :param type: String (Optional) - Type of projector: `Preview` (default), `Source`, `Scene`, `StudioProgram`, or
        `Multiview` (case insensitive).
        :param monitor: int (Optional) - Monitor to open the projector on. If -1 or omitted, opens a window.
        :param geometry: String (Optional) - Size and position of the projector window (only if monitor is -1). Encoded
        in Base64 using [Qt's geometry encoding](https://doc.qt.io/qt-5/qwidget.html#saveGeometry). Corresponds to OBS's
        saved projectors.
        :param name: String (Optional) - Name of the source or scene to be displayed (ignored for other projector
        types).

    """
    return __createJSON("OpenProjector", {'type': type, 'monitor': monitor, 'geometry': geometry, 'name': name})


def triggerHotkeyByName(hotkeyName: str):
    """
    Executes hotkey routine, identified by hotkey unique name

        :param hotkeyName: String - Unique name of the hotkey, as defined when registering the hotkey
        (e.g. "ReplayBuffer.Save")

    """
    return __createJSON("TriggerHotkeyByName", {'hotkeyName': hotkeyName})


def triggerHotkeyBySequence(keyId: str, keyModifiers: Object = {}):
    """
    Executes hotkey routine, identified by bound combination of keys. A single key combination might trigger multiple
    hotkey routines depending on user settings

    :param keyId: String - Main key identifier (e.g. `OBS_KEY_A` for key "A"). Available identifiers
    [here](https://github.com/obsproject/obs-studio/blob/master/libobs/obs-hotkeys.h)
    :param keyModifiers: Object (Optional) - Optional key modifiers object. False entries can be ommitted

    """
    return __createJSON("TriggerHotkeyBySequence", {'keyId': keyId, 'keyModifiers': keyModifiers})


def executeBatch(requests: List[Object], abortOnFail: bool = False):
    """
    Executes a list of requests sequentially (one-by-one on the same thread).

    :param requests: Array<Object> - Array of requests to perform. Executed in order.
    - requests.*.request_type: String - Request type. Eg. `GetVersion`.
    - requests.*.message_id: String (Optional) - ID of the individual request. Can be any string and not required to be
    unique. Defaults to empty string if not specified.
    :param abortOnFail: boolean (Optional) - Stop processing batch requests if one returns a failure.

    """
    return __createJSON("ExecuteBatch", {'requests': requests, 'abortOnFail': abortOnFail})


def sleep(sleepMillis: int):
    """
    Waits for the specified duration. Designed to be used in `ExecuteBatch` operations.

        :param sleepMillis: int - Delay in milliseconds to wait before continuing.

    """
    return __createJSON("Sleep", {'sleepMillis': sleepMillis})


# endregion

# region MEDIA CONTROL
def playPauseMedia(sourceName: str, playPause: bool):
    """
    Pause or play a media source. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)
    Note :Leaving out `playPause` toggles the current pause state

        :param sourceName: String - Source name.
        :param playPause: boolean - (optional) Whether to pause or play the source. `false` for play, `true` for pause.

    """
    return __createJSON("PlayPauseMedia", {'sourceName': sourceName, 'playPause': playPause})


def restartMedia(sourceName: str):
    """
    Restart a media source. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)

        :param sourceName: String - Source name.

    """
    return __createJSON("RestartMedia", {'sourceName': sourceName})


def stopMedia(sourceName: str):
    """
    Stop a media source. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)

        :param sourceName: String - Source name.

    """
    return __createJSON("StopMedia", {'sourceName': sourceName})


def nextMedia(sourceName: str):
    """
    Skip to the next media item in the playlist. Supports only vlc media source (as of OBS v25.0.8)

        :param sourceName: String - Source name.

    """
    return __createJSON("NextMedia", {'sourceName': sourceName})


def previousMedia(sourceName: str):
    """
    Go to the previous media item in the playlist. Supports only vlc media source (as of OBS v25.0.8)

        :param sourceName: String - Source name.

    """
    return __createJSON("PreviousMedia", {'sourceName': sourceName})


def getMediaDuration(sourceName: str):
    """
    Get the length of media in milliseconds. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)
    Note: For some reason, for the first 5 or so seconds that the media is playing, the total duration can be off by
    upwards of 50ms.

        :param sourceName: String - Source name.

    """
    return __createJSON("GetMediaDuration", {'sourceName': sourceName})


def getMediaTime(sourceName: str):
    """
    Get the current timestamp of media in milliseconds. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)

        :param sourceName: String - Source name.

    """
    return __createJSON("GetMediaTime", {'sourceName': sourceName})


def setMediaTime(sourceName: str, timestamp: int):
    """
    Set the timestamp of a media source. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)

        :param sourceName: String - Source name.
        :param timestamp: int - Milliseconds to set the timestamp to.

    """
    return __createJSON("SetMediaTime", {'sourceName': sourceName, 'timestamp': timestamp})


def scrubMedia(sourceName: str, timeOffset: int):
    """
    Scrub media using a supplied offset. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)
    Note: Due to processing/network delays, this request is not perfect. The processing rate of this request has also
    not been tested.

        :param sourceName: String - Source name.
        :param timeOffset: int - Millisecond offset (positive or negative) to offset the current media position.

    """
    return __createJSON("ScrubMedia", {'sourceName': sourceName, 'timeOffset': timeOffset})


def getMediaState(sourceName: str):
    """
    Get the current playing state of a media source. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)

        :param sourceName: String - Source name.

    """
    return __createJSON("GetMediaState", {'sourceName': sourceName})


# endregion

# region SOURCES
def getMediaSourcesList():
    """
    List the media state of all media sources (vlc and media source)


    """
    return __createJSON("GetMediaSourcesList", {})


def createSource(sourceName: str, sourceKind: str, sceneName: str, sourceSettings: Object = {},
                 setVisible: bool = False):
    """
    Create a source and add it as a sceneitem to a scene.

        :param sourceName: String - Source name.
        :param sourceKind: String - Source kind, Eg. `vlc_source`.
        :param sceneName: String - Scene to add the new source to.
        :param sourceSettings: Object (optional) - Source settings data.
        :param setVisible: boolean (optional) - Set the created SceneItem as visible or not. Defaults to true

    """
    return __createJSON("CreateSource", {'sourceName': sourceName, 'sourceKind': sourceKind, 'sceneName': sceneName,
                                         'sourceSettings': sourceSettings, 'setVisible': setVisible})


def getSourcesList():
    """
    List all sources available in the running OBS instance


    """
    return __createJSON("GetSourcesList", {})


def getSourceTypesList():
    """
    Get a list of all available sources types


    """
    return __createJSON("GetSourceTypesList", {})


def getVolume(source: str, useDecibel: bool = False):
    """
    Get the volume of the specified source. Default response uses mul format, NOT SLIDER PERCENTAGE.

        :param source: String - Source name.
        :param useDecibel: boolean (optional) - Output volume in decibels of attenuation instead of amplitude/mul.

    """
    return __createJSON("GetVolume", {'source': source, 'useDecibel': useDecibel})


def setVolume(source: str, volume: float, useDecibel: bool = False):
    """
    Set the volume of the specified source. Default request format uses mul, NOT SLIDER PERCENTAGE.

        :param source: String - Source name.
        :param volume: double - Desired volume. Must be between `0.0` and `20.0` for mul, and under 26.0 for dB. OBS
        will interpret dB values under -100.0 as Inf. Note: The OBS volume sliders only reach a maximum of 1.0mul/0.0dB,
        however OBS actually supports larger values.
        :param useDecibel: boolean (optional) - Interperet `volume` data as decibels instead of amplitude/mul.

    """
    return __createJSON("SetVolume", {'source': source, 'volume': volume, 'useDecibel': useDecibel})
4

def setAudioTracks(sourceName: str, track: int, active: bool):
    """
    Changes whether an audio track is active for a source.

        :param sourceName: String - Source name.
        :param track: int - Audio tracks 1-6.
        :param active: boolean - Whether audio track is active or not.

    """
    return __createJSON("SetAudioTracks", {'sourceName': sourceName, 'track': track, 'active': active})


def getAudioTracks(sourceName: str):
    """
    Gets whether an audio track is active for a source.

        :param sourceName: String - Source name.

    """
    return __createJSON("GetAudioTracks", {'sourceName': sourceName})


def getMute(source: str):
    """
    Get the mute status of a specified source.

        :param source: String - Source name.

    """
    return __createJSON("GetMute", {'source': source})


def setMute(source: str, mute: bool):
    """
    Sets the mute status of a specified source.

        :param source: String - Source name.
        :param mute: boolean - Desired mute status.

    """
    return __createJSON("SetMute", {'source': source, 'mute': mute})


def toggleMute(source: str):
    """
    Inverts the mute status of a specified source.

        :param source: String - Source name.

    """
    return __createJSON("ToggleMute", {'source': source})


def getSourceActive(sourceName: str):
    """
    Get the source's active status of a specified source (if it is showing in the final mix).

        :param sourceName: String - Source name.

    """
    return __createJSON("GetSourceActive", {'sourceName': sourceName})


def getAudioActive(sourceName: str):
    """
    Get the audio's active status of a specified source.

        :param sourceName: String - Source name.

    """
    return __createJSON("GetAudioActive", {'sourceName': sourceName})


def setSourceName(sourceName: str, newName: str):
    """


    Note: If the new name already exists as a source, obs-websocket will return an error.

        :param sourceName: String - Source name.
        :param newName: String - New source name.

    """
    return __createJSON("SetSourceName", {'sourceName': sourceName, 'newName': newName})


def setSyncOffset(source: str, offset: int):
    """
    Set the audio sync offset of a specified source.

        :param source: String - Source name.
        :param offset: int - The desired audio sync offset (in nanoseconds).

    """
    return __createJSON("SetSyncOffset", {'source': source, 'offset': offset})


def getSyncOffset(source: str):
    """
    Get the audio sync offset of a specified source.

        :param source: String - Source name.

    """
    return __createJSON("GetSyncOffset", {'source': source})


def getSourceSettings(sourceName: str, sourceType: str = ''):
    """
    Get settings of the specified source

        :param sourceName: String - Source name.
        :param sourceType: String (optional) - Type of the specified source. Useful for type-checking if you expect a
        specific settings schema.

    """
    return __createJSON("GetSourceSettings", {'sourceName': sourceName, 'sourceType': sourceType})


def setSourceSettings(sourceName: str, sourceSettings: Object, sourceType: str = ''):
    """
    Set settings of the specified source.

        :param sourceName: String - Source name.
        :param sourceSettings: Object - Source settings (varies between source types, may require some probing around).
        :param sourceType: String (optional) - Type of the specified source. Useful for type-checking to avoid settings
        a set of settings incompatible with the actual source's type.

    """
    return __createJSON("SetSourceSettings",
                        {'sourceName': sourceName, 'sourceSettings': sourceSettings, 'sourceType': sourceType})


def getTextGDIPlusProperties(source: str):
    """
    Get the current properties of a Text GDI Plus source.

        :param source: String - Source name.

    """
    return __createJSON("GetTextGDIPlusProperties", {'source': source})


def setTextGDIPlusProperties(source: str, align: str = '', bk_color: int = 0, bk_opacity: int = 0,
                             chatlog: bool = False, chatlog_lines: int = 0, color: int = 0, extents: bool = False,
                             extents_cx: int = 0, extents_cy: int = 0, file: str = '', read_from_file: bool = False,
                             font: Object = {}, gradient: bool = False, gradient_color: int = 0,
                             gradient_dir: float = 0.0, gradient_opacity: int = 0, outline: bool = False,
                             outline_color: int = 0, outline_size: int = 0, outline_opacity: int = 0, text: str = '',
                             valign: str = '', vertical: bool = False, render: bool = False):
    """
    Set the current properties of a Text GDI Plus source.

        :param source: String - Name of the source.
        :param align: String (optional) - Text Alignment ("left", "center", "right").
        :param bk_color: int (optional) - Background color.
        :param bk_opacity: int (optional) - Background opacity (0-100).
        :param chatlog: boolean (optional) - Chat log.
        :param chatlog_lines: int (optional) - Chat log lines.
        :param color: int (optional) - Text color.
        :param extents: boolean (optional) - Extents wrap.
        :param extents_cx: int (optional) - Extents cx.
        :param extents_cy: int (optional) - Extents cy.
        :param file: String (optional) - File path name.
        :param read_from_file: boolean (optional) - Read text from the specified file.
        :param font: Object (optional) - Holds data for the font. Ex: `"font": { "face": "Arial", "flags": 0,
        "size": 150, "style": "" }`
        - font.face: String (optional) - Font face.
        - font.flags: int (optional) - Font text styling flag. `Bold=1, Italic=2, Bold Italic=3, Underline=5,
        Strikeout=8`
        - font.size: int (optional) - Font text size.
        - font.style: String (optional) - Font Style (unknown function).
        :param gradient: boolean (optional) - Gradient enabled.
        :param gradient_color: int (optional) - Gradient color.
        :param gradient_dir: float (optional) - Gradient direction.
        :param gradient_opacity: int (optional) - Gradient opacity (0-100).
        :param outline: boolean (optional) - Outline.
        :param outline_color: int (optional) - Outline color.
        :param outline_size: int (optional) - Outline size.
        :param outline_opacity: int (optional) - Outline opacity (0-100).
        :param text: String (optional) - Text content to be displayed.
        :param valign: String (optional) - Text vertical alignment ("top", "center", "bottom").
        :param vertical: boolean (optional) - Vertical text enabled.
        :param render: boolean (optional) - Visibility of the scene item.

    """
    return __createJSON("SetTextGDIPlusProperties",
                        {'source': source, 'align': align, 'bk_color': bk_color, 'bk_opacity': bk_opacity,
                         'chatlog': chatlog, 'chatlog_lines': chatlog_lines, 'color': color, 'extents': extents,
                         'extents_cx': extents_cx, 'extents_cy': extents_cy, 'file': file,
                         'read_from_file': read_from_file,
                         'font': font, 'gradient': gradient, 'gradient_color': gradient_color,
                         'gradient_dir': gradient_dir, 'gradient_opacity': gradient_opacity, 'outline': outline,
                         'outline_color': outline_color, 'outline_size': outline_size,
                         'outline_opacity': outline_opacity,
                         'text': text, 'valign': valign, 'vertical': vertical, 'render': render})


def getTextFreetype2Properties(source: str):
    """
    Get the current properties of a Text Freetype 2 source.

        :param source: String - Source name.

    """
    return __createJSON("GetTextFreetype2Properties", {'source': source})


def setTextFreetype2Properties(source: str, color1: int = 0, color2: int = 0, custom_width: int = 0,
                               drop_shadow: bool = False, font: Object = {}, from_file: bool = False,
                               log_mode: bool = False, outline: bool = False, text: str = '', text_file: str = '',
                               word_wrap: bool = False):
    """
    Set the current properties of a Text Freetype 2 source.

        :param source: String - Source name.
        :param color1: int (optional) - Gradient top color.
        :param color2: int (optional) - Gradient bottom color.
        :param custom_width: int (optional) - Custom width (0 to disable).
        :param drop_shadow: boolean (optional) - Drop shadow.
        :param font: Object (optional) - Holds data for the font. Ex: `"font": { "face": "Arial", "flags": 0,
        "size": 150, "style": "" }`
        - font.face: String (optional) - Font face.
        - font.flags: int (optional) - Font text styling flag. `Bold=1, Italic=2, Bold Italic=3, Underline=5,
        Strikeout=8`
        - font.size: int (optional) - Font text size.
        - font.style: String (optional) - Font Style (unknown function).
        :param from_file: boolean (optional) - Read text from the specified file.
        :param log_mode: boolean (optional) - Chat log.
        :param outline: boolean (optional) - Outline.
        :param text: String (optional) - Text content to be displayed.
        :param text_file: String (optional) - File path.
        :param word_wrap: boolean (optional) - Word wrap.

    """
    return __createJSON("SetTextFreetype2Properties",
                        {'source': source, 'color1': color1, 'color2': color2, 'custom_width': custom_width,
                         'drop_shadow': drop_shadow, 'font': font, 'from_file': from_file, 'log_mode': log_mode,
                         'outline': outline, 'text': text, 'text_file': text_file, 'word_wrap': word_wrap})


def getBrowserSourceProperties(source: str):
    """
    Get current properties for a Browser Source.

        :param source: String - Source name.

    """
    return __createJSON("GetBrowserSourceProperties", {'source': source})


def setBrowserSourceProperties(source: str, is_local_file: bool = False, local_file: str = '', url: str = '',
                               css: str = '', width: int = 0, height: int = 0, fps: int = 0, shutdown: bool = False,
                               render: bool = False):
    """
    Set current properties for a Browser Source.

        :param source: String - Name of the source.
        :param is_local_file: boolean (optional) - Indicates that a local file is in use.
        :param local_file: String (optional) - file path.
        :param url: String (optional) - Url.
        :param css: String (optional) - CSS to inject.
        :param width: int (optional) - Width.
        :param height: int (optional) - Height.
        :param fps: int (optional) - Framerate.
        :param shutdown: boolean (optional) - Indicates whether the source should be shutdown when not visible.
        :param render: boolean (optional) - Visibility of the scene item.

    """
    return __createJSON("SetBrowserSourceProperties",
                        {'source': source, 'is_local_file': is_local_file, 'local_file': local_file, 'url': url,
                         'css': css, 'width': width, 'height': height, 'fps': fps, 'shutdown': shutdown,
                         'render': render})


def getSpecialSources():
    """
    Get configured special sources like Desktop Audio and Mic/Aux sources.


    """
    return __createJSON("GetSpecialSources", {})


def getSourceFilters(sourceName: str):
    """
    List filters applied to a source

        :param sourceName: String - Source name

    """
    return __createJSON("GetSourceFilters", {'sourceName': sourceName})


def getSourceFilterInfo(sourceName: str, filterName: str):
    """
    List filters applied to a source

        :param sourceName: String - Source name
        :param filterName: String - Source filter name

    """
    return __createJSON("GetSourceFilterInfo", {'sourceName': sourceName, 'filterName': filterName})


def addFilterToSource(sourceName: str, filterName: str, filterType: str, filterSettings: Object):
    """
    Add a new filter to a source. Available source types along with their settings properties are available from
    `GetSourceTypesList`.

        :param sourceName: String - Name of the source on which the filter is added
        :param filterName: String - Name of the new filter
        :param filterType: String - Filter type
        :param filterSettings: Object - Filter settings

    """
    return __createJSON("AddFilterToSource",
                        {'sourceName': sourceName, 'filterName': filterName, 'filterType': filterType,
                         'filterSettings': filterSettings})


def removeFilterFromSource(sourceName: str, filterName: str):
    """
    Remove a filter from a source

        :param sourceName: String - Name of the source from which the specified filter is removed
        :param filterName: String - Name of the filter to remove

    """
    return __createJSON("RemoveFilterFromSource", {'sourceName': sourceName, 'filterName': filterName})


def reorderSourceFilter(sourceName: str, filterName: str, newIndex: int):
    """
    Move a filter in the chain (absolute index positioning)

        :param sourceName: String - Name of the source to which the filter belongs
        :param filterName: String - Name of the filter to reorder
        :param newIndex: Integer - Desired position of the filter in the chain

    """
    return __createJSON("ReorderSourceFilter",
                        {'sourceName': sourceName, 'filterName': filterName, 'newIndex': newIndex})


def moveSourceFilter(sourceName: str, filterName: str, movementType: str):
    """
    Move a filter in the chain (relative positioning)

        :param sourceName: String - Name of the source to which the filter belongs
        :param filterName: String - Name of the filter to reorder
        :param movementType: String - How to move the filter around in the source's filter chain. Either "up", "down",
        "top" or "bottom".

    """
    return __createJSON("MoveSourceFilter",
                        {'sourceName': sourceName, 'filterName': filterName, 'movementType': movementType})


def setSourceFilterSettings(sourceName: str, filterName: str, filterSettings: Object):
    """
    Update settings of a filter

        :param sourceName: String - Name of the source to which the filter belongs
        :param filterName: String - Name of the filter to reconfigure
        :param filterSettings: Object - New settings. These will be merged to the current filter settings.

    """
    return __createJSON("SetSourceFilterSettings",
                        {'sourceName': sourceName, 'filterName': filterName, 'filterSettings': filterSettings})


def setSourceFilterVisibility(sourceName: str, filterName: str, filterEnabled: bool):
    """
    Change the visibility/enabled state of a filter

        :param sourceName: String - Source name
        :param filterName: String - Source filter name
        :param filterEnabled: Boolean - New filter state

    """
    return __createJSON("SetSourceFilterVisibility",
                        {'sourceName': sourceName, 'filterName': filterName, 'filterEnabled': filterEnabled})


def getAudioMonitorType(sourceName: str):
    """
    Get the audio monitoring type of the specified source.

        :param sourceName: String - Source name.

    """
    return __createJSON("GetAudioMonitorType", {'sourceName': sourceName})


def setAudioMonitorType(sourceName: str, monitorType: str):
    """
    Set the audio monitoring type of the specified source.

        :param sourceName: String - Source name.
        :param monitorType: String - The monitor type to use. Options: `none`, `monitorOnly`, `monitorAndOutput`.

    """
    return __createJSON("SetAudioMonitorType", {'sourceName': sourceName, 'monitorType': monitorType})


def getSourceDefaultSettings(sourceKind: str):
    """
    Get the default settings for a given source type.

        :param sourceKind: String - Source kind. Also called "source id" in libobs terminology.

    """
    return __createJSON("GetSourceDefaultSettings", {'sourceKind': sourceKind})


def takeSourceScreenshot(sourceName: str = '', embedPictureFormat: str = '', saveToFilePath: str = '',
                         fileFormat: str = '', compressionQuality: int = 0, width: int = 0, height: int = 0):
    """


    At least `embedPictureFormat` or `saveToFilePath` must be specified.

    Clients can specify `width` and `height` parameters to receive scaled pictures. Aspect ratio is
    preserved if only one of these two parameters is specified.

        :param sourceName: String (optional) - Source name. Note: Since scenes are also sources, you can also provide a
        scene name. If not provided, the currently active scene is used.
        :param embedPictureFormat: String (optional) - Format of the Data URI encoded picture. Can be "png", "jpg",
        "jpeg" or "bmp" (or any other value supported by Qt's Image module)
        :param saveToFilePath: String (optional) - Full file path (file extension included) where the captured image is
        to be saved. Can be in a format different from `pictureFormat`. Can be a relative path.
        :param fileFormat: String (optional) - Format to save the image file as (one of the values provided in the
        `supported-image-export-formats` response field of `GetVersion`). If not specified, tries to guess based on
        file extension.
        :param compressionQuality: int (optional) - Compression ratio between -1 and 100 to write the image with. -1 is
        automatic, 1 is smallest file/most compression, 100 is largest file/least compression. Varies with image type.
        :param width: int (optional) - Screenshot width. Defaults to the source's base width.
        :param height: int (optional) - Screenshot height. Defaults to the source's base height.

    """
    return __createJSON("TakeSourceScreenshot", {'sourceName': sourceName, 'embedPictureFormat': embedPictureFormat,
                                                 'saveToFilePath': saveToFilePath, 'fileFormat': fileFormat,
                                                 'compressionQuality': compressionQuality, 'width': width,
                                                 'height': height})


def refreshBrowserSource(sourceName: str):
    """
    Refreshes the specified browser source.

        :param sourceName: String - Source name.

    """
    return __createJSON("RefreshBrowserSource", {'sourceName': sourceName})


# endregion

# region OUTPUTS
def listOutputs():
    """
    List existing outputs


    """
    return __createJSON("ListOutputs", {})


def getOutputInfo(outputName: str):
    """
    Get information about a single output

        :param outputName: String - Output name

    """
    return __createJSON("GetOutputInfo", {'outputName': outputName})


def startOutput(outputName: str):
    """


    Note: Controlling outputs is an experimental feature of obs-websocket. Some plugins which add outputs to OBS may not
    function properly when they are controlled in this way.

        :param outputName: String - Output name

    """
    return __createJSON("StartOutput", {'outputName': outputName})


def stopOutput(outputName: str, force: bool = False):
    """


    Note: Controlling outputs is an experimental feature of obs-websocket. Some plugins which add outputs to OBS may not
    function properly when they are controlled in this way.

        :param outputName: String - Output name
        :param force: boolean (optional) - Force stop (default: false)

    """
    return __createJSON("StopOutput", {'outputName': outputName, 'force': force})


# endregion

# region PROFILES
def setCurrentProfile(profile_name: str):
    """
    Set the currently active profile.

        :param profile_name: String - Name of the desired profile.

    """
    return __createJSON("SetCurrentProfile", {'profile-name': profile_name})


def getCurrentProfile():
    """
    Get the name of the current profile.


    """
    return __createJSON("GetCurrentProfile", {})


def listProfiles():
    """
    Get a list of available profiles.


    """
    return __createJSON("ListProfiles", {})


# endregion

# region RECORDING
def getRecordingStatus():
    """
    Get current recording status.


    """
    return __createJSON("GetRecordingStatus", {})


def startStopRecording():
    """
    Toggle recording on or off (depending on the current recording state).


    """
    return __createJSON("StartStopRecording", {})


def startRecording():
    """
    Start recording.
    Will return an `error` if recording is already active.


    """
    return __createJSON("StartRecording", {})


def stopRecording():
    """
    Stop recording.
    Will return an `error` if recording is not active.


    """
    return __createJSON("StopRecording", {})


def pauseRecording():
    """
    Pause the current recording.
    Returns an error if recording is not active or already paused.


    """
    return __createJSON("PauseRecording", {})


def resumeRecording():
    """
    Resume/unpause the current recording (if paused).
    Returns an error if recording is not active or not paused.


    """
    return __createJSON("ResumeRecording", {})


def setRecordingFolder(rec_folder: str):
    """


    Note: If `SetRecordingFolder` is called while a recording is
    in progress, the change won't be applied immediately and will be
    effective on the next recording.

        :param rec_folder: String - Path of the recording folder.

    """
    return __createJSON("SetRecordingFolder", {'rec-folder': rec_folder})


def getRecordingFolder():
    """
    Get the path of  the current recording folder.


    """
    return __createJSON("GetRecordingFolder", {})


# endregion

# region REPLAY BUFFER
def getReplayBufferStatus():
    """
    Get the status of the OBS replay buffer.


    """
    return __createJSON("GetReplayBufferStatus", {})


def startStopReplayBuffer():
    """
    Toggle the Replay Buffer on/off (depending on the current state of the replay buffer).


    """
    return __createJSON("StartStopReplayBuffer", {})


def startReplayBuffer():
    """
    Start recording into the Replay Buffer.
    Will return an `error` if the Replay Buffer is already active or if the
    "Save Replay Buffer" hotkey is not set in OBS' settings.
    Setting this hotkey is mandatory, even when triggering saves only
    through obs-websocket.


    """
    return __createJSON("StartReplayBuffer", {})


def stopReplayBuffer():
    """
    Stop recording into the Replay Buffer.
    Will return an `error` if the Replay Buffer is not active.


    """
    return __createJSON("StopReplayBuffer", {})


def saveReplayBuffer():
    """
    Flush and save the contents of the Replay Buffer to disk. This is
    basically the same as triggering the "Save Replay Buffer" hotkey.
    Will return an `error` if the Replay Buffer is not active.


    """
    return __createJSON("SaveReplayBuffer", {})


# endregion

# region SCENE COLLECTIONS
def setCurrentSceneCollection(sc_name: str):
    """
    Change the active scene collection.

        :param sc_name: String - Name of the desired scene collection.

    """
    return __createJSON("SetCurrentSceneCollection", {'sc-name': sc_name})


def getCurrentSceneCollection():
    """
    Get the name of the current scene collection.


    """
    return __createJSON("GetCurrentSceneCollection", {})


def listSceneCollections():
    """
    List available scene collections


    """
    return __createJSON("ListSceneCollections", {})


# endregion

# region SCENE ITEMS
def getSceneItemList(sceneName: str = ''):
    """
    Get a list of all scene items in a scene.

        :param sceneName: String (optional) - Name of the scene to get the list of scene items from. Defaults to the
        current scene if not specified.

    """
    return __createJSON("GetSceneItemList", {'sceneName': sceneName})


def getSceneItemProperties(item: Union[str, Object], scene_name: str = ''):
    """
    Gets the scene specific properties of the specified source item.
    Coordinates are relative to the item's parent (the scene or group it belongs to).

        :param item: String | Object - Scene Item name (if this field is a string) or specification
        (if it is an object).
        - item.name: String (optional) - Scene Item name (if the `item` field is an object)
        - item.id: int (optional) - Scene Item ID (if the `item` field is an object)
        :param scene_name: String (optional) - Name of the scene the scene item belongs to. Defaults to the current
        scene.

    """
    return __createJSON("GetSceneItemProperties",
                        {'item': item, 'scene-name': scene_name})


def setSceneItemProperties(item: Union[str, Object], scene_name: str = '',
                           position_x: float = 0.0, position_y: float = 0.0, position_alignment: int = 0,
                           rotation: float = 0.0,
                           scale_x: float = 0.0, scale_y: float = 0.0, scale_filter: str = '',
                           crop_top: int = 0, crop_bottom: int = 0, crop_left: int = 0, crop_right: int = 0,
                           visible: bool = False,
                           locked: bool = False,
                           bounds_type: str = '', bounds_alignment: int = 0,
                           bounds_x: float = 0.0, bounds_y: float = 0.0):
    """
    Sets the scene specific properties of a source. Unspecified properties will remain unchanged.
    Coordinates are relative to the item's parent (the scene or group it belongs to).

        :param item: String | Object - Scene Item name (if this field is a string) or specification
        (if it is an object)
.
        :param scene_name: String (optional) - Name of the scene the source item belongs to. Defaults to the current
        scene.
        - item.name: String (optional) - Scene Item name (if the `item` field is an object)
        - item.id: int (optional) - Scene Item ID (if the `item` field is an object)

        :param position_x: double (optional) - The new x position of the source.
        :param position_y: double (optional) - The new y position of the source.
        :param position_alignment: int (optional) - The new alignment of the source.
        :param rotation: double (optional) - The new clockwise rotation of the item in degrees.
        :param scale_x: double (optional) - The new x scale of the item.
        :param scale_y: double (optional) - The new y scale of the item.
        :param scale_filter: String (optional) - The new scale filter of the source. Can be "OBS_SCALE_DISABLE",
        "OBS_SCALE_POINT", "OBS_SCALE_BICUBIC", "OBS_SCALE_BILINEAR", "OBS_SCALE_LANCZOS" or "OBS_SCALE_AREA".
        :param crop_top: int (optional) - The new amount of pixels cropped off the top of the source before scaling.
        :param crop_bottom: int (optional) - The new amount of pixels cropped off the bottom of the source before
        scaling.
        :param crop_left: int (optional) - The new amount of pixels cropped off the left of the source before scaling.
        :param crop_right: int (optional) - The new amount of pixels cropped off the right of the source before scaling.
        :param visible: bool (optional) - The new visibility of the source. 'true' shows source, 'false' hides source.
        :param locked: bool (optional) - The new locked status of the source. 'true' keeps it in its current position,
        'false' allows movement.
        :param bounds_type: String (optional) - The new bounds type of the source. Can be "OBS_BOUNDS_STRETCH",
        "OBS_BOUNDS_SCALE_INNER", "OBS_BOUNDS_SCALE_OUTER", "OBS_BOUNDS_SCALE_TO_WIDTH", "OBS_BOUNDS_SCALE_TO_HEIGHT",
        "OBS_BOUNDS_MAX_ONLY" or "OBS_BOUNDS_NONE".
        :param bounds_alignment: int (optional) - The new alignment of the bounding box. (0-2, 4-6, 8-10)
        :param bounds_x: double (optional) - The new width of the bounding box.
        :param bounds_y: double (optional) - The new height of the bounding box.

    """
    return __createJSON("SetSceneItemProperties",
                        {'item': item, 'scene-name': scene_name,
                         'position.x': position_x, 'position.y': position_y, 'position.alignment': position_alignment,
                         'rotation': rotation, 'scale.x': scale_x, 'scale.y': scale_y, 'scale.filter': scale_filter,
                         'crop.top': crop_top, 'crop.bottom': crop_bottom, 'crop.left': crop_left,
                         'crop.right': crop_right,
                         'visible': visible, 'locked': locked, 'bounds.type': bounds_type,
                         'bounds.alignment': bounds_alignment, 'bounds.x': bounds_x, 'bounds.y': bounds_y})


def setSceneItemPropertiesFromDict(item: Union[str, Object], scene_name: str = '', properties=None):
    """
    Sets the scene specific properties of a source. Unspecified properties will remain unchanged.
    Coordinates are relative to the item's parent (the scene or group it belongs to).

        :param item: String | Object - Scene Item name (if this field is a string) or specification
        (if it is an object)
.
        :param scene_name: String (optional) - Name of the scene the source item belongs to. Defaults to the current
        scene.
        - item.name: String (optional) - Scene Item name (if the `item` field is an object)
        - item.id: int (optional) - Scene Item ID (if the `item` field is an object)

        :param properties: Dictionary of SceneItem Properties
    """

    if properties is not None:
        properties = deepcopy(properties)
    else:
        properties = {}

    properties['scene-name'] = scene_name
    properties['item'] = item

    return __createJSON("SetSceneItemProperties", properties)


def resetSceneItem(item: Union[str, Object], scene_name: str = ''):
    """
    Reset a scene item.

        :param item: String | Object - Scene Item name (if this field is a string) or specification
        (if it is an object).
        - item.name: String (optional) - Scene Item name (if the `item` field is an object)
        - item.id: int (optional) - Scene Item ID (if the `item` field is an object)
        :param scene_name: String (optional) - Name of the scene the scene item belongs to. Defaults to the current
        scene.


    """
    return __createJSON("ResetSceneItem", {'item': item, 'scene-name': scene_name})


def setSceneItemRender(render: bool, scene_name: str = '', source: str = '', item: int = 0):
    """
    Show or hide a specified source item in a specified scene.

        :param render: boolean - true = shown ; false = hidden
        :param scene_name: String (optional) - Name of the scene the scene item belongs to. Defaults to the currently
        active scene.
        :param source: String (optional) - Scene Item name.
        :param item: int (optional) - Scene Item id

    """
    return __createJSON("SetSceneItemRender",
                        {'render': render, 'scene-name': scene_name, 'source': source, 'item': item})


def setSceneItemPosition(item: str, x: float, y: float, scene_name: str = ''):
    """
    Sets the coordinates of a specified source item.

        :param item: String - Scene Item name.
        :param x: double - X coordinate.
        :param y: double - Y coordinate.
        :param scene_name: String (optional) - Name of the scene the scene item belongs to. Defaults to the current
        scene.

    """
    return __createJSON("SetSceneItemPosition", {'item': item, 'x': x, 'y': y, 'scene-name': scene_name})


def setSceneItemTransform(item: str, x_scale: float, y_scale: float, rotation: float, scene_name: str = ''):
    """
    Set the transform of the specified source item.

        :param item: String - Scene Item name.
        :param x_scale: double - Width scale factor.
        :param y_scale: double - Height scale factor.
        :param rotation: double - Source item rotation (in degrees).
        :param scene_name: String (optional) - Name of the scene the scene item belongs to. Defaults to the current
        scene.

    """
    return __createJSON("SetSceneItemTransform",
                        {'item': item, 'x-scale': x_scale, 'y-scale': y_scale, 'rotation': rotation,
                         'scene-name': scene_name})


def setSceneItemCrop(item: str, top: int, bottom: int, left: int, right: int, scene_name: str = ''):
    """
    Sets the crop coordinates of the specified source item.

        :param item: String - Scene Item name.
        :param top: int - Pixel position of the top of the source item.
        :param bottom: int - Pixel position of the bottom of the source item.
        :param left: int - Pixel position of the left of the source item.
        :param right: int - Pixel position of the right of the source item.
        :param scene_name: String (optional) - Name of the scene the scene item belongs to. Defaults to the current
        scene.

    """
    return __createJSON("SetSceneItemCrop", {'item': item, 'top': top, 'bottom': bottom, 'left': left, 'right': right,
                                             'scene-name': scene_name})


def deleteSceneItem(item: Object, scene: str = ''):
    """
    Deletes a scene item.

        :param item: Object - Scene item to delete (required)
        - item.name: String - Scene Item name (prefer `id`, including both is acceptable).
        - item.id: int - Scene Item ID.
        :param scene: String (optional) - Name of the scene the scene item belongs to. Defaults to the current scene.

    """
    return __createJSON("DeleteSceneItem", {'item': item, 'scene': scene})


def addSceneItem(sceneName: str, sourceName: str, setVisible: bool = False):
    """
    Creates a scene item in a scene. In other words, this is how you add a source into a scene.

        :param sceneName: String - Name of the scene to create the scene item in
        :param sourceName: String - Name of the source to be added
        :param setVisible: boolean (optional) - Whether to make the sceneitem visible on creation or not. Default `true`
    """
    return __createJSON("AddSceneItem", {'sceneName': sceneName, 'sourceName': sourceName, 'setVisible': setVisible})


def duplicateSceneItem(item: Object, fromScene: str = '', toScene: str = ''):
    """
    Duplicates a scene item.

        :param item: Object - Scene Item to duplicate from the source scene (required)
        - item.name: String - Scene Item name (prefer `id`, including both is acceptable).
        - item.id: int - Scene Item ID.
        :param fromScene: String (optional) - Name of the scene to copy the item from. Defaults to the current scene.
        :param toScene: String (optional) - Name of the scene to create the item in. Defaults to the current scene.

    """
    return __createJSON("DuplicateSceneItem",
                        {'item': item, 'fromScene': fromScene,
                         'toScene': toScene})


# endregion

# region SCENES
def setCurrentScene(scene_name: str):
    """
    Switch to the specified scene.

        :param scene_name: String - Name of the scene to switch to.

    """
    return __createJSON("SetCurrentScene", {'scene-name': scene_name})


def getCurrentScene():
    """
    Get the current scene's name and source items.


    """
    return __createJSON("GetCurrentScene", {})


def getSceneList():
    """
    Get a list of scenes in the currently active profile.


    """
    return __createJSON("GetSceneList", {})


def createScene(sceneName: str):
    """
    Create a new scene scene.

        :param sceneName: String - Name of the scene to create.

    """
    return __createJSON("CreateScene", {'sceneName': sceneName})


def reorderSceneItems(items: List[Object], scene: str = ''):
    """
    Changes the order of scene items in the requested scene.

        :param items: Array<Object> - Ordered list of objects with name and/or id specified. Id preferred due to
        uniqueness per scene
        :param scene: String (optional) - Name of the scene to reorder (defaults to current).
        - items.*.id: int (optional) - Id of a specific scene item. Unique on a scene by scene basis.
        - items.*.name: String (optional) - Name of a scene item. Sufficiently unique if no scene items share sources
        within the scene.

    """
    return __createJSON("ReorderSceneItems", {'items': items, 'scene': scene})


def setSceneTransitionOverride(sceneName: str, transitionName: str, transitionDuration: int = 0):
    """
    Set a scene to use a specific transition override.

        :param sceneName: String - Name of the scene to switch to.
        :param transitionName: String - Name of the transition to use.
        :param transitionDuration: int (Optional) - Duration in milliseconds of the transition if transition is not
        fixed. Defaults to the current duration specified in the UI if there is no current override and this value is
        not given.

    """
    return __createJSON("SetSceneTransitionOverride", {'sceneName': sceneName, 'transitionName': transitionName,
                                                       'transitionDuration': transitionDuration})


def removeSceneTransitionOverride(sceneName: str):
    """
    Remove any transition override on a scene.

        :param sceneName: String - Name of the scene to switch to.

    """
    return __createJSON("RemoveSceneTransitionOverride", {'sceneName': sceneName})


def getSceneTransitionOverride(sceneName: str):
    """
    Get the current scene transition override.

        :param sceneName: String - Name of the scene to switch to.

    """
    return __createJSON("GetSceneTransitionOverride", {'sceneName': sceneName})


# endregion

# region STREAMING
def getStreamingStatus():
    """
    Get current streaming and recording status.
    """
    return __createJSON("GetStreamingStatus", {})


def startStopStreaming():
    """
    Toggle streaming on or off (depending on the current stream state).


    """
    return __createJSON("StartStopStreaming", {})


def startStreaming(stream: Object = {}):
    """
    Start streaming.
    Will return an `error` if streaming is already active.

        :param stream: Object (optional) - Special stream configuration. Note: these won't be saved to OBS'
        configuration.
        - stream.type: String (optional) - If specified ensures the type of stream matches the given type (usually
        'rtmp_custom' or 'rtmp_common'). If the currently configured stream type does not match the given stream type,
        all settings must be specified in the `settings` object or an error will occur when starting the stream.
        - stream.metadata: Object (optional) - Adds the given object parameters as encoded query string parameters to
        the 'key' of the RTMP stream. Used to pass data to the RTMP service about the streaming. May be any String,
        Numeric, or Boolean field.
        - stream.settings: Object (optional) - Settings for the stream.
        - stream.settings.server: String (optional) - The publish URL.
        - stream.settings.key: String (optional) - The publish key of the stream.
        - stream.settings.use_auth: boolean (optional) - Indicates whether authentication should be used when connecting
        to the streaming server.
        - stream.settings.username: String (optional) - If authentication is enabled, the username for the streaming
        server. Ignored if `use_auth` is not set to `true`.
        - stream.settings.password: String (optional) - If authentication is enabled, the password for the streaming
        server. Ignored if `use_auth` is not set to `true`.

    """
    return __createJSON("StartStreaming", {'stream': stream})


def stopStreaming():
    """
    Stop streaming.
    Will return an `error` if streaming is not active.


    """
    return __createJSON("StopStreaming", {})


def setStreamSettings(type: str, settings: Object, save: bool):
    """
    Sets one or more attributes of the current streaming server settings. Any options not passed will remain unchanged.
    Returns the updated settings in response. If 'type' is different than the current streaming service type, all
    settings are required. Returns the full settings of the stream (the same as GetStreamSettings).

        :param type: String - The type of streaming service configuration, usually `rtmp_custom` or `rtmp_common`.
        :param settings: Object - The actual settings of the stream.
        :param save: boolean - Persist the settings to disk.
        - settings.server: String (optional) - The publish URL.
        - settings.key: String (optional) - The publish key.
        - settings.use_auth: boolean (optional) - Indicates whether authentication should be used when connecting to the
         streaming server.
        - settings.username: String (optional) - The username for the streaming service.
        - settings.password: String (optional) - The password for the streaming service.

    """
    return __createJSON("SetStreamSettings", {'type': type, 'settings': settings, 'save': save})


def getStreamSettings():
    """
    Get the current streaming server settings.

    """
    return __createJSON("GetStreamSettings", {})


def saveStreamSettings():
    """
    Save the current streaming server settings to disk.


    """
    return __createJSON("SaveStreamSettings", {})


def sendCaptions(text: str):
    """
    Send the provided text as embedded CEA-608 caption data.

        :param text: String - Captions text

    """
    return __createJSON("SendCaptions", {'text': text})


# endregion

# region STUDIO MODE
def getStudioModeStatus():
    """
    Indicates if Studio Mode is currently enabled.


    """
    return __createJSON("GetStudioModeStatus", {})


def getPreviewScene():
    """
    Get the name of the currently previewed scene and its list of sources.
    Will return an `error` if Studio Mode is not enabled.


    """
    return __createJSON("GetPreviewScene", {})


def setPreviewScene(scene_name: str):
    """
    Set the active preview scene.
    Will return an `error` if Studio Mode is not enabled.

        :param scene_name: String - The name of the scene to preview.

    """
    return __createJSON("SetPreviewScene", {'scene-name': scene_name})


def transitionToProgram(with_transition: Object = {}):
    """
    Transitions the currently previewed scene to the main output.
    Will return an `error` if Studio Mode is not enabled.

        :param with_transition: Object (optional) - Change the active transition before switching scenes. Defaults to
        the active transition.
        - with_transition.name: String - Name of the transition.
        - with_transition.duration: int (optional) - Transition duration (in milliseconds).

    """
    return __createJSON("TransitionToProgram", {'with-transition': with_transition})


def enableStudioMode():
    """
    Enables Studio Mode.


    """
    return __createJSON("EnableStudioMode", {})


def disableStudioMode():
    """
    Disables Studio Mode.


    """
    return __createJSON("DisableStudioMode", {})


def toggleStudioMode():
    """
    Toggles Studio Mode (depending on the current state of studio mode).


    """
    return __createJSON("ToggleStudioMode", {})


# endregion

# region TRANSITIONS
def getTransitionList():
    """
    List of all transitions available in the frontend's dropdown menu.


    """
    return __createJSON("GetTransitionList", {})


def getCurrentTransition():
    """
    Get the name of the currently selected transition in the frontend's dropdown menu.


    """
    return __createJSON("GetCurrentTransition", {})


def setCurrentTransition(transition_name: str):
    """
    Set the active transition.

        :param transition_name: String - The name of the transition.

    """
    return __createJSON("SetCurrentTransition", {'transition-name': transition_name})


def setTransitionDuration(duration: int):
    """
    Set the duration of the currently selected transition if supported.

        :param duration: int - Desired duration of the transition (in milliseconds).

    """
    return __createJSON("SetTransitionDuration", {'duration': duration})


def getTransitionDuration():
    """
    Get the duration of the currently selected transition if supported.


    """
    return __createJSON("GetTransitionDuration", {})


def getTransitionPosition():
    """
    Get the position of the current transition.


    """
    return __createJSON("GetTransitionPosition", {})


def getTransitionSettings(transitionName: str):
    """
    Get the current settings of a transition

        :param transitionName: String - Transition name

    """
    return __createJSON("GetTransitionSettings", {'transitionName': transitionName})


def setTransitionSettings(transitionName: str, transitionSettings: Object):
    """
    Change the current settings of a transition

        :param transitionName: String - Transition name
        :param transitionSettings: Object - Transition settings (they can be partial)

    """
    return __createJSON("SetTransitionSettings",
                        {'transitionName': transitionName, 'transitionSettings': transitionSettings})


def releaseTBar():
    """
    Release the T-Bar (like a user releasing their mouse button after moving it).
    *YOU MUST CALL THIS if you called `SetTBarPosition` with the `release` parameter set to `false`.*


    """
    return __createJSON("ReleaseTBar", {})


def setTBarPosition(position: float, release: bool = False):
    """


    If your code needs to perform multiple successive T-Bar moves (e.g. : in an animation, or in response to a user
    moving a T-Bar control in your User Interface), set `release` to false and call `ReleaseTBar` later once the
    animation/interaction is over.

        :param position: double - T-Bar position. This value must be between 0.0 and 1.0.
        :param release: boolean (optional) - Whether or not the T-Bar gets released automatically after setting its new
        position (like a user releasing their mouse button after moving the T-Bar). Call `ReleaseTBar` manually if you
        set `release` to false. Defaults to true.

    """
    return __createJSON("SetTBarPosition", {'position': position, 'release': release})


# endregion

# region VIRTUAL CAM
def getVirtualCamStatus():
    """
    Get current virtual cam status.


    """
    return __createJSON("GetVirtualCamStatus", {})


def startStopVirtualCam():
    """
    Toggle virtual cam on or off (depending on the current virtual cam state).


    """
    return __createJSON("StartStopVirtualCam", {})


def startVirtualCam():
    """
    Start virtual cam.
    Will return an `error` if virtual cam is already active.


    """
    return __createJSON("StartVirtualCam", {})


def stopVirtualCam():
    """
    Stop virtual cam.
    Will return an `error` if virtual cam is not active.


    """
    return __createJSON("StopVirtualCam", {})

# endregion
