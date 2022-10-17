from typing import Any, Dict, List, Union, Optional

__MESSAGE_ID = 0

Object = Dict[str, Any]

def getMessageID() -> str:
    """
    Generates a message id unique to this session
    :return: the generated message id
    """
    global __MESSAGE_ID
    ret = "PY_WSCTRL-" + hex(__MESSAGE_ID)
    __MESSAGE_ID = __MESSAGE_ID + 1
    return ret

def __createMessage(requestType: str, data=None) -> dict:
    """
    :param requestType: Request Type
    :param data: Additional data fields for the request
    :return: A dictionary containing all message fields
    """
    result = {}
    d = {}

    if data is None:
        data = {}

    d["requestType"] = requestType
    d["requestId"] = getMessageID()
    d["requestData"] = data

    result["op"] = 6 # Request OPCode is constant 6
    result["d"] = d

    return result

#region CONFIG
def getPersistentData(realm: str, slotName: str):
    """
    Gets the value of a "slot" from the selected persistent data realm.
    
    :param realm: String - The data realm to select. 'OBS_WEBSOCKET_DATA_REALM_GLOBAL' or 'OBS_WEBSOCKET_DATA_REALM_PROFILE'
    :param slotName: String - The name of the slot to retrieve data from
    
    """
    params = {}
    params['realm'] = realm
    params['slotName'] = slotName
    
    return __createMessage("GetPersistentData", params)


def setPersistentData(realm: str, slotName: str, slotValue: Any):
    """
    Sets the value of a "slot" from the selected persistent data realm.
    
    :param realm: String - The data realm to select. 'OBS_WEBSOCKET_DATA_REALM_GLOBAL' or 'OBS_WEBSOCKET_DATA_REALM_PROFILE'
    :param slotName: String - The name of the slot to retrieve data from
    :param slotValue: Any - The value to apply to the slot
    
    """
    params = {}
    params['realm'] = realm
    params['slotName'] = slotName
    params['slotValue'] = slotValue
    
    return __createMessage("SetPersistentData", params)


def getSceneCollectionList():
    """
    Gets an array of all scene collections
    
    
    """
    params = {}
    
    return __createMessage("GetSceneCollectionList", params)


def setCurrentSceneCollection(sceneCollectionName: str):
    """
    Switches to a scene collection.
    
    Note: This will block until the collection has finished changing.
    
    :param sceneCollectionName: String - Name of the scene collection to switch to
    
    """
    params = {}
    params['sceneCollectionName'] = sceneCollectionName
    
    return __createMessage("SetCurrentSceneCollection", params)


def createSceneCollection(sceneCollectionName: str):
    """
    Creates a new scene collection, switching to it in the process.
    
    Note: This will block until the collection has finished changing.
    
    :param sceneCollectionName: String - Name for the new scene collection
    
    """
    params = {}
    params['sceneCollectionName'] = sceneCollectionName
    
    return __createMessage("CreateSceneCollection", params)


def getProfileList():
    """
    Gets an array of all profiles
    
    
    """
    params = {}
    
    return __createMessage("GetProfileList", params)


def setCurrentProfile(profileName: str):
    """
    Switches to a profile.
    
    :param profileName: String - Name of the profile to switch to
    
    """
    params = {}
    params['profileName'] = profileName
    
    return __createMessage("SetCurrentProfile", params)


def createProfile(profileName: str):
    """
    Creates a new profile, switching to it in the process
    
    :param profileName: String - Name for the new profile
    
    """
    params = {}
    params['profileName'] = profileName
    
    return __createMessage("CreateProfile", params)


def removeProfile(profileName: str):
    """
    Removes a profile. If the current profile is chosen, it will change to a different profile first.
    
    :param profileName: String - Name of the profile to remove
    
    """
    params = {}
    params['profileName'] = profileName
    
    return __createMessage("RemoveProfile", params)


def getProfileParameter(parameterCategory: str, parameterName: str):
    """
    Gets a parameter from the current profile's configuration.
    
    :param parameterCategory: String - Category of the parameter to get
    :param parameterName: String - Name of the parameter to get
    
    """
    params = {}
    params['parameterCategory'] = parameterCategory
    params['parameterName'] = parameterName
    
    return __createMessage("GetProfileParameter", params)


def setProfileParameter(parameterCategory: str, parameterName: str, parameterValue: str):
    """
    Sets the value of a parameter in the current profile's configuration.
    
    :param parameterCategory: String - Category of the parameter to set
    :param parameterName: String - Name of the parameter to set
    :param parameterValue: String - Value of the parameter to set. Use 'null' to delete
    
    """
    params = {}
    params['parameterCategory'] = parameterCategory
    params['parameterName'] = parameterName
    params['parameterValue'] = parameterValue
    
    return __createMessage("SetProfileParameter", params)


def getVideoSettings():
    """
    Gets the current video settings.
    
    Note: To get the true FPS value, divide the FPS numerator by the FPS denominator. Example: '60000/1001'
    
    
    """
    params = {}
    
    return __createMessage("GetVideoSettings", params)


def setVideoSettings(fpsNumerator: Optional[Union[int, float]] = None, fpsDenominator: Optional[Union[int, float]] = None, baseWidth: Optional[Union[int, float]] = None, baseHeight: Optional[Union[int, float]] = None, outputWidth: Optional[Union[int, float]] = None, outputHeight: Optional[Union[int, float]] = None):
    """
    Sets the current video settings.
    
    Note: Fields must be specified in pairs. For example, you cannot set only 'baseWidth' without needing to specify 'baseHeight'.
    
    :param fpsNumerator: Number (Optional) - Numerator of the fractional FPS value	Restrictions: >= 1	Optional Behaviour: Not changed
    :param fpsDenominator: Number (Optional) - Denominator of the fractional FPS value	Restrictions: >= 1	Optional Behaviour: Not changed
    :param baseWidth: Number (Optional) - Width of the base (canvas) resolution in pixels	Restrictions: >= 1, <= 4096	Optional Behaviour: Not changed
    :param baseHeight: Number (Optional) - Height of the base (canvas) resolution in pixels	Restrictions: >= 1, <= 4096	Optional Behaviour: Not changed
    :param outputWidth: Number (Optional) - Width of the output resolution in pixels	Restrictions: >= 1, <= 4096	Optional Behaviour: Not changed
    :param outputHeight: Number (Optional) - Height of the output resolution in pixels	Restrictions: >= 1, <= 4096	Optional Behaviour: Not changed
    
    """
    params = {}
    if fpsNumerator is not None:
        params['fpsNumerator'] = fpsNumerator
    if fpsDenominator is not None:
        params['fpsDenominator'] = fpsDenominator
    if baseWidth is not None:
        params['baseWidth'] = baseWidth
    if baseHeight is not None:
        params['baseHeight'] = baseHeight
    if outputWidth is not None:
        params['outputWidth'] = outputWidth
    if outputHeight is not None:
        params['outputHeight'] = outputHeight
    
    return __createMessage("SetVideoSettings", params)


def getStreamServiceSettings():
    """
    Gets the current stream service settings (stream destination).
    
    
    """
    params = {}
    
    return __createMessage("GetStreamServiceSettings", params)


def setStreamServiceSettings(streamServiceType: str, streamServiceSettings: Object):
    """
    Sets the current stream service settings (stream destination).
    
    Note: Simple RTMP settings can be set with type 'rtmp_custom' and the settings fields 'server' and 'key'.
    
    :param streamServiceType: String - Type of stream service to apply. Example: 'rtmp_common' or 'rtmp_custom'
    :param streamServiceSettings: Object - Settings to apply to the service
    
    """
    params = {}
    params['streamServiceType'] = streamServiceType
    params['streamServiceSettings'] = streamServiceSettings
    
    return __createMessage("SetStreamServiceSettings", params)


def getRecordDirectory():
    """
    Gets the current directory that the record output is set to.
    
    
    """
    params = {}
    
    return __createMessage("GetRecordDirectory", params)


#endregion

#region FILTERS
def getSourceFilterList(sourceName: str):
    """
    Gets an array of all of a source's filters.
    
    :param sourceName: String - Name of the source
    
    """
    params = {}
    params['sourceName'] = sourceName
    
    return __createMessage("GetSourceFilterList", params)


def getSourceFilterDefaultSettings(filterKind: str):
    """
    Gets the default settings for a filter kind.
    
    :param filterKind: String - Filter kind to get the default settings for
    
    """
    params = {}
    params['filterKind'] = filterKind
    
    return __createMessage("GetSourceFilterDefaultSettings", params)


def createSourceFilter(sourceName: str, filterName: str, filterKind: str, filterSettings: Optional[Object] = None):
    """
    Creates a new filter, adding it to the specified source.
    
    :param sourceName: String - Name of the source to add the filter to
    :param filterName: String - Name of the new filter to be created
    :param filterKind: String - The kind of filter to be created
    :param filterSettings: Object (Optional) - Settings object to initialize the filter with	Optional Behaviour: Default settings used
    
    """
    params = {}
    params['sourceName'] = sourceName
    params['filterName'] = filterName
    params['filterKind'] = filterKind
    if filterSettings is not None:
        params['filterSettings'] = filterSettings
    
    return __createMessage("CreateSourceFilter", params)


def removeSourceFilter(sourceName: str, filterName: str):
    """
    Removes a filter from a source.
    
    :param sourceName: String - Name of the source the filter is on
    :param filterName: String - Name of the filter to remove
    
    """
    params = {}
    params['sourceName'] = sourceName
    params['filterName'] = filterName
    
    return __createMessage("RemoveSourceFilter", params)


def setSourceFilterName(sourceName: str, filterName: str, newFilterName: str):
    """
    Sets the name of a source filter (rename).
    
    :param sourceName: String - Name of the source the filter is on
    :param filterName: String - Current name of the filter
    :param newFilterName: String - New name for the filter
    
    """
    params = {}
    params['sourceName'] = sourceName
    params['filterName'] = filterName
    params['newFilterName'] = newFilterName
    
    return __createMessage("SetSourceFilterName", params)


def getSourceFilter(sourceName: str, filterName: str):
    """
    Gets the info for a specific source filter.
    
    :param sourceName: String - Name of the source
    :param filterName: String - Name of the filter
    
    """
    params = {}
    params['sourceName'] = sourceName
    params['filterName'] = filterName
    
    return __createMessage("GetSourceFilter", params)


def setSourceFilterIndex(sourceName: str, filterName: str, filterIndex: Union[int, float]):
    """
    Sets the index position of a filter on a source.
    
    :param sourceName: String - Name of the source the filter is on
    :param filterName: String - Name of the filter
    :param filterIndex: Number - New index position of the filter	Restrictions: >= 0
    
    """
    params = {}
    params['sourceName'] = sourceName
    params['filterName'] = filterName
    params['filterIndex'] = filterIndex
    
    return __createMessage("SetSourceFilterIndex", params)


def setSourceFilterSettings(sourceName: str, filterName: str, filterSettings: Object, overlay: Optional[bool] = None):
    """
    Sets the settings of a source filter.
    
    :param sourceName: String - Name of the source the filter is on
    :param filterName: String - Name of the filter to set the settings of
    :param filterSettings: Object - Object of settings to apply
    :param overlay: Boolean (Optional) - True == apply the settings on top of existing ones, False == reset the input to its defaults, then apply settings.	Optional Behaviour: true
    
    """
    params = {}
    params['sourceName'] = sourceName
    params['filterName'] = filterName
    params['filterSettings'] = filterSettings
    if overlay is not None:
        params['overlay'] = overlay
    
    return __createMessage("SetSourceFilterSettings", params)


def setSourceFilterEnabled(sourceName: str, filterName: str, filterEnabled: bool):
    """
    Sets the enable state of a source filter.
    
    :param sourceName: String - Name of the source the filter is on
    :param filterName: String - Name of the filter
    :param filterEnabled: Boolean - New enable state of the filter
    
    """
    params = {}
    params['sourceName'] = sourceName
    params['filterName'] = filterName
    params['filterEnabled'] = filterEnabled
    
    return __createMessage("SetSourceFilterEnabled", params)


#endregion

#region GENERAL
def getVersion():
    """
    Gets data about the current plugin and RPC version.
    
    
    """
    params = {}
    
    return __createMessage("GetVersion", params)


def getStats():
    """
    Gets statistics about OBS, obs-websocket, and the current session.
    
    
    """
    params = {}
    
    return __createMessage("GetStats", params)


def broadcastCustomEvent(eventData: Object):
    """
    Broadcasts a 'CustomEvent' to all WebSocket clients. Receivers are clients which are identified and subscribed.
    
    :param eventData: Object - Data payload to emit to all receivers
    
    """
    params = {}
    params['eventData'] = eventData
    
    return __createMessage("BroadcastCustomEvent", params)


def callVendorRequest(vendorName: str, requestType: str, requestData: Optional[Object] = None):
    """
    Call a request registered to a vendor.
    
    A vendor is a unique name registered by a third-party plugin or script, which allows for custom requests and events to be added to obs-websocket.
    If a plugin or script implements vendor requests or events, documentation is expected to be provided with them.
    
    :param vendorName: String - Name of the vendor to use
    :param requestType: String - The request type to call
    :param requestData: Object (Optional) - Object containing appropriate request data	Optional Behaviour: {}
    
    """
    params = {}
    params['vendorName'] = vendorName
    params['requestType'] = requestType
    if requestData is not None:
        params['requestData'] = requestData
    
    return __createMessage("CallVendorRequest", params)


def getHotkeyList():
    """
    Gets an array of all hotkey names in OBS
    
    
    """
    params = {}
    
    return __createMessage("GetHotkeyList", params)


def triggerHotkeyByName(hotkeyName: str):
    """
    Triggers a hotkey using its name. See 'GetHotkeyList'
    
    :param hotkeyName: String - Name of the hotkey to trigger
    
    """
    params = {}
    params['hotkeyName'] = hotkeyName
    
    return __createMessage("TriggerHotkeyByName", params)


def triggerHotkeyByKeySequence(keyId: Optional[str] = None, keyModifiers: Optional[Object] = None, keyModifiers_shift: Optional[bool] = None, keyModifiers_control: Optional[bool] = None, keyModifiers_alt: Optional[bool] = None, keyModifiers_command: Optional[bool] = None):
    """
    Triggers a hotkey using a sequence of keys.
    
    :param keyId: String (Optional) - The OBS key ID to use. See https://github.com/obsproject/obs-studio/blob/master/libobs/obs-hotkeys.h	Optional Behaviour: Not pressed
    :param keyModifiers: Object (Optional) - Object containing key modifiers to apply	Optional Behaviour: Ignored
    :param keyModifiers_shift: Boolean (Optional) - Press Shift	Optional Behaviour: Not pressed
    :param keyModifiers_control: Boolean (Optional) - Press CTRL	Optional Behaviour: Not pressed
    :param keyModifiers_alt: Boolean (Optional) - Press ALT	Optional Behaviour: Not pressed
    :param keyModifiers_command: Boolean (Optional) - Press CMD (Mac)	Optional Behaviour: Not pressed
    
    """
    params = {}
    if keyId is not None:
        params['keyId'] = keyId
    if keyModifiers is not None:
        params['keyModifiers'] = keyModifiers
    if params['keyModifiers'] is None:
        params['keyModifiers'] = {}
    if keyModifiers_shift is not None:
        params['keyModifiers']['shift'] = keyModifiers_shift
    if keyModifiers_control is not None:
        params['keyModifiers']['control'] = keyModifiers_control
    if keyModifiers_alt is not None:
        params['keyModifiers']['alt'] = keyModifiers_alt
    if keyModifiers_command is not None:
        params['keyModifiers']['command'] = keyModifiers_command
    
    return __createMessage("TriggerHotkeyByKeySequence", params)


def sleep(sleepMillis: Union[int, float], sleepFrames: Union[int, float]):
    """
    Sleeps for a time duration or number of frames. Only available in request batches with types 'SERIAL_REALTIME' or 'SERIAL_FRAME'.
    
    :param sleepMillis: Number - Number of milliseconds to sleep for (if 'SERIAL_REALTIME' mode)	Restrictions: >= 0, <= 50000
    :param sleepFrames: Number - Number of frames to sleep for (if 'SERIAL_FRAME' mode)	Restrictions: >= 0, <= 10000
    
    """
    params = {}
    params['sleepMillis'] = sleepMillis
    params['sleepFrames'] = sleepFrames
    
    return __createMessage("Sleep", params)


#endregion

#region INPUTS
def getInputList(inputKind: Optional[str] = None):
    """
    Gets an array of all inputs in OBS.
    
    :param inputKind: String (Optional) - Restrict the array to only inputs of the specified kind	Optional Behaviour: All kinds included
    
    """
    params = {}
    if inputKind is not None:
        params['inputKind'] = inputKind
    
    return __createMessage("GetInputList", params)


def getInputKindList(unversioned: Optional[bool] = None):
    """
    Gets an array of all available input kinds in OBS.
    
    :param unversioned: Boolean (Optional) - True == Return all kinds as unversioned, False == Return with version suffixes (if available)	Optional Behaviour: false
    
    """
    params = {}
    if unversioned is not None:
        params['unversioned'] = unversioned
    
    return __createMessage("GetInputKindList", params)


def getSpecialInputs():
    """
    Gets the names of all special inputs.
    
    
    """
    params = {}
    
    return __createMessage("GetSpecialInputs", params)


def createInput(sceneName: str, inputName: str, inputKind: str, inputSettings: Optional[Object] = None, sceneItemEnabled: Optional[bool] = None):
    """
    Creates a new input, adding it as a scene item to the specified scene.
    
    :param sceneName: String - Name of the scene to add the input to as a scene item
    :param inputName: String - Name of the new input to created
    :param inputKind: String - The kind of input to be created
    :param inputSettings: Object (Optional) - Settings object to initialize the input with	Optional Behaviour: Default settings used
    :param sceneItemEnabled: Boolean (Optional) - Whether to set the created scene item to enabled or disabled	Optional Behaviour: True
    
    """
    params = {}
    params['sceneName'] = sceneName
    params['inputName'] = inputName
    params['inputKind'] = inputKind
    if inputSettings is not None:
        params['inputSettings'] = inputSettings
    if sceneItemEnabled is not None:
        params['sceneItemEnabled'] = sceneItemEnabled
    
    return __createMessage("CreateInput", params)


def removeInput(inputName: str):
    """
    Removes an existing input.
    
    Note: Will immediately remove all associated scene items.
    
    :param inputName: String - Name of the input to remove
    
    """
    params = {}
    params['inputName'] = inputName
    
    return __createMessage("RemoveInput", params)


def setInputName(inputName: str, newInputName: str):
    """
    Sets the name of an input (rename).
    
    :param inputName: String - Current input name
    :param newInputName: String - New name for the input
    
    """
    params = {}
    params['inputName'] = inputName
    params['newInputName'] = newInputName
    
    return __createMessage("SetInputName", params)


def getInputDefaultSettings(inputKind: str):
    """
    Gets the default settings for an input kind.
    
    :param inputKind: String - Input kind to get the default settings for
    
    """
    params = {}
    params['inputKind'] = inputKind
    
    return __createMessage("GetInputDefaultSettings", params)


def getInputSettings(inputName: str):
    """
    Gets the settings of an input.
    
    Note: Does not include defaults. To create the entire settings object, overlay 'inputSettings' over the 'defaultInputSettings' provided by 'GetInputDefaultSettings'.
    
    :param inputName: String - Name of the input to get the settings of
    
    """
    params = {}
    params['inputName'] = inputName
    
    return __createMessage("GetInputSettings", params)


def setInputSettings(inputName: str, inputSettings: Object, overlay: Optional[bool] = None):
    """
    Sets the settings of an input.
    
    :param inputName: String - Name of the input to set the settings of
    :param inputSettings: Object - Object of settings to apply
    :param overlay: Boolean (Optional) - True == apply the settings on top of existing ones, False == reset the input to its defaults, then apply settings.	Optional Behaviour: true
    
    """
    params = {}
    params['inputName'] = inputName
    params['inputSettings'] = inputSettings
    if overlay is not None:
        params['overlay'] = overlay
    
    return __createMessage("SetInputSettings", params)


def getInputMute(inputName: str):
    """
    Gets the audio mute state of an input.
    
    :param inputName: String - Name of input to get the mute state of
    
    """
    params = {}
    params['inputName'] = inputName
    
    return __createMessage("GetInputMute", params)


def setInputMute(inputName: str, inputMuted: bool):
    """
    Sets the audio mute state of an input.
    
    :param inputName: String - Name of the input to set the mute state of
    :param inputMuted: Boolean - Whether to mute the input or not
    
    """
    params = {}
    params['inputName'] = inputName
    params['inputMuted'] = inputMuted
    
    return __createMessage("SetInputMute", params)


def toggleInputMute(inputName: str):
    """
    Toggles the audio mute state of an input.
    
    :param inputName: String - Name of the input to toggle the mute state of
    
    """
    params = {}
    params['inputName'] = inputName
    
    return __createMessage("ToggleInputMute", params)


def getInputVolume(inputName: str):
    """
    Gets the current volume setting of an input.
    
    :param inputName: String - Name of the input to get the volume of
    
    """
    params = {}
    params['inputName'] = inputName
    
    return __createMessage("GetInputVolume", params)


def setInputVolume(inputName: str, inputVolumeMul: Optional[Union[int, float]] = None, inputVolumeDb: Optional[Union[int, float]] = None):
    """
    Sets the volume setting of an input.
    
    :param inputName: String - Name of the input to set the volume of
    :param inputVolumeMul: Number (Optional) - Volume setting in mul	Restrictions: >= 0, <= 20	Optional Behaviour: 'inputVolumeDb' should be specified
    :param inputVolumeDb: Number (Optional) - Volume setting in dB	Restrictions: >= -100, <= 26	Optional Behaviour: 'inputVolumeMul' should be specified
    
    """
    params = {}
    params['inputName'] = inputName
    if inputVolumeMul is not None:
        params['inputVolumeMul'] = inputVolumeMul
    if inputVolumeDb is not None:
        params['inputVolumeDb'] = inputVolumeDb
    
    return __createMessage("SetInputVolume", params)


def getInputAudioBalance(inputName: str):
    """
    Gets the audio balance of an input.
    
    :param inputName: String - Name of the input to get the audio balance of
    
    """
    params = {}
    params['inputName'] = inputName
    
    return __createMessage("GetInputAudioBalance", params)


def setInputAudioBalance(inputName: str, inputAudioBalance: Union[int, float]):
    """
    Sets the audio balance of an input.
    
    :param inputName: String - Name of the input to set the audio balance of
    :param inputAudioBalance: Number - New audio balance value	Restrictions: >= 0.0, <= 1.0
    
    """
    params = {}
    params['inputName'] = inputName
    params['inputAudioBalance'] = inputAudioBalance
    
    return __createMessage("SetInputAudioBalance", params)


def getInputAudioSyncOffset(inputName: str):
    """
    Gets the audio sync offset of an input.
    
    Note: The audio sync offset can be negative too!
    
    :param inputName: String - Name of the input to get the audio sync offset of
    
    """
    params = {}
    params['inputName'] = inputName
    
    return __createMessage("GetInputAudioSyncOffset", params)


def setInputAudioSyncOffset(inputName: str, inputAudioSyncOffset: Union[int, float]):
    """
    Sets the audio sync offset of an input.
    
    :param inputName: String - Name of the input to set the audio sync offset of
    :param inputAudioSyncOffset: Number - New audio sync offset in milliseconds	Restrictions: >= -950, <= 20000
    
    """
    params = {}
    params['inputName'] = inputName
    params['inputAudioSyncOffset'] = inputAudioSyncOffset
    
    return __createMessage("SetInputAudioSyncOffset", params)


def getInputAudioMonitorType(inputName: str):
    """
    Gets the audio monitor type of an input.
    
    The available audio monitor types are:
    
    - 'OBS_MONITORING_TYPE_NONE'
    - 'OBS_MONITORING_TYPE_MONITOR_ONLY'
    - 'OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT'
    
    :param inputName: String - Name of the input to get the audio monitor type of
    
    """
    params = {}
    params['inputName'] = inputName
    
    return __createMessage("GetInputAudioMonitorType", params)


def setInputAudioMonitorType(inputName: str, monitorType: str):
    """
    Sets the audio monitor type of an input.
    
    :param inputName: String - Name of the input to set the audio monitor type of
    :param monitorType: String - Audio monitor type
    
    """
    params = {}
    params['inputName'] = inputName
    params['monitorType'] = monitorType
    
    return __createMessage("SetInputAudioMonitorType", params)


def getInputAudioTracks(inputName: str):
    """
    Gets the enable state of all audio tracks of an input.
    
    :param inputName: String - Name of the input
    
    """
    params = {}
    params['inputName'] = inputName
    
    return __createMessage("GetInputAudioTracks", params)


def setInputAudioTracks(inputName: str, inputAudioTracks: Object):
    """
    Sets the enable state of audio tracks of an input.
    
    :param inputName: String - Name of the input
    :param inputAudioTracks: Object - Track settings to apply
    
    """
    params = {}
    params['inputName'] = inputName
    params['inputAudioTracks'] = inputAudioTracks
    
    return __createMessage("SetInputAudioTracks", params)


def getInputPropertiesListPropertyItems(inputName: str, propertyName: str):
    """
    Gets the items of a list property from an input's properties.
    
    Note: Use this in cases where an input provides a dynamic, selectable list of items. For example, display capture, where it provides a list of available displays.
    
    :param inputName: String - Name of the input
    :param propertyName: String - Name of the list property to get the items of
    
    """
    params = {}
    params['inputName'] = inputName
    params['propertyName'] = propertyName
    
    return __createMessage("GetInputPropertiesListPropertyItems", params)


def pressInputPropertiesButton(inputName: str, propertyName: str):
    """
    Presses a button in the properties of an input.
    
    Some known 'propertyName' values are:
    
    - 'refreshnocache' - Browser source reload button
    
    Note: Use this in cases where there is a button in the properties of an input that cannot be accessed in any other way. For example, browser sources, where there is a refresh button.
    
    :param inputName: String - Name of the input
    :param propertyName: String - Name of the button property to press
    
    """
    params = {}
    params['inputName'] = inputName
    params['propertyName'] = propertyName
    
    return __createMessage("PressInputPropertiesButton", params)


#endregion

#region MEDIA INPUTS
def getMediaInputStatus(inputName: str):
    """
    Gets the status of a media input.
    
    Media States:
    
    - 'OBS_MEDIA_STATE_NONE'
    - 'OBS_MEDIA_STATE_PLAYING'
    - 'OBS_MEDIA_STATE_OPENING'
    - 'OBS_MEDIA_STATE_BUFFERING'
    - 'OBS_MEDIA_STATE_PAUSED'
    - 'OBS_MEDIA_STATE_STOPPED'
    - 'OBS_MEDIA_STATE_ENDED'
    - 'OBS_MEDIA_STATE_ERROR'
    
    :param inputName: String - Name of the media input
    
    """
    params = {}
    params['inputName'] = inputName
    
    return __createMessage("GetMediaInputStatus", params)


def setMediaInputCursor(inputName: str, mediaCursor: Union[int, float]):
    """
    Sets the cursor position of a media input.
    
    This request does not perform bounds checking of the cursor position.
    
    :param inputName: String - Name of the media input
    :param mediaCursor: Number - New cursor position to set	Restrictions: >= 0
    
    """
    params = {}
    params['inputName'] = inputName
    params['mediaCursor'] = mediaCursor
    
    return __createMessage("SetMediaInputCursor", params)


def offsetMediaInputCursor(inputName: str, mediaCursorOffset: Union[int, float]):
    """
    Offsets the current cursor position of a media input by the specified value.
    
    This request does not perform bounds checking of the cursor position.
    
    :param inputName: String - Name of the media input
    :param mediaCursorOffset: Number - Value to offset the current cursor position by
    
    """
    params = {}
    params['inputName'] = inputName
    params['mediaCursorOffset'] = mediaCursorOffset
    
    return __createMessage("OffsetMediaInputCursor", params)


def triggerMediaInputAction(inputName: str, mediaAction: str):
    """
    Triggers an action on a media input.
    
    :param inputName: String - Name of the media input
    :param mediaAction: String - Identifier of the 'ObsMediaInputAction' enum
    
    """
    params = {}
    params['inputName'] = inputName
    params['mediaAction'] = mediaAction
    
    return __createMessage("TriggerMediaInputAction", params)


#endregion

#region OUTPUTS
def getVirtualCamStatus():
    """
    Gets the status of the virtualcam output.
    
    
    """
    params = {}
    
    return __createMessage("GetVirtualCamStatus", params)


def toggleVirtualCam():
    """
    Toggles the state of the virtualcam output.
    
    
    """
    params = {}
    
    return __createMessage("ToggleVirtualCam", params)


def startVirtualCam():
    """
    Starts the virtualcam output.
    
    
    """
    params = {}
    
    return __createMessage("StartVirtualCam", params)


def stopVirtualCam():
    """
    Stops the virtualcam output.
    
    
    """
    params = {}
    
    return __createMessage("StopVirtualCam", params)


def getReplayBufferStatus():
    """
    Gets the status of the replay buffer output.
    
    
    """
    params = {}
    
    return __createMessage("GetReplayBufferStatus", params)


def toggleReplayBuffer():
    """
    Toggles the state of the replay buffer output.
    
    
    """
    params = {}
    
    return __createMessage("ToggleReplayBuffer", params)


def startReplayBuffer():
    """
    Starts the replay buffer output.
    
    
    """
    params = {}
    
    return __createMessage("StartReplayBuffer", params)


def stopReplayBuffer():
    """
    Stops the replay buffer output.
    
    
    """
    params = {}
    
    return __createMessage("StopReplayBuffer", params)


def saveReplayBuffer():
    """
    Saves the contents of the replay buffer output.
    
    
    """
    params = {}
    
    return __createMessage("SaveReplayBuffer", params)


def getLastReplayBufferReplay():
    """
    Gets the filename of the last replay buffer save file.
    
    
    """
    params = {}
    
    return __createMessage("GetLastReplayBufferReplay", params)


def getOutputList():
    """
    Gets the list of available outputs.
    
    
    """
    params = {}
    
    return __createMessage("GetOutputList", params)


def getOutputStatus(outputName: str):
    """
    Gets the status of an output.
    
    :param outputName: String - Output name
    
    """
    params = {}
    params['outputName'] = outputName
    
    return __createMessage("GetOutputStatus", params)


def toggleOutput(outputName: str):
    """
    Toggles the status of an output.
    
    :param outputName: String - Output name
    
    """
    params = {}
    params['outputName'] = outputName
    
    return __createMessage("ToggleOutput", params)


def startOutput(outputName: str):
    """
    Starts an output.
    
    :param outputName: String - Output name
    
    """
    params = {}
    params['outputName'] = outputName
    
    return __createMessage("StartOutput", params)


def stopOutput(outputName: str):
    """
    Stops an output.
    
    :param outputName: String - Output name
    
    """
    params = {}
    params['outputName'] = outputName
    
    return __createMessage("StopOutput", params)


def getOutputSettings(outputName: str):
    """
    Gets the settings of an output.
    
    :param outputName: String - Output name
    
    """
    params = {}
    params['outputName'] = outputName
    
    return __createMessage("GetOutputSettings", params)


def setOutputSettings(outputName: str, outputSettings: Object):
    """
    Sets the settings of an output.
    
    :param outputName: String - Output name
    :param outputSettings: Object - Output settings
    
    """
    params = {}
    params['outputName'] = outputName
    params['outputSettings'] = outputSettings
    
    return __createMessage("SetOutputSettings", params)


#endregion

#region RECORD
def getRecordStatus():
    """
    Gets the status of the record output.
    
    
    """
    params = {}
    
    return __createMessage("GetRecordStatus", params)


def toggleRecord():
    """
    Toggles the status of the record output.
    
    
    """
    params = {}
    
    return __createMessage("ToggleRecord", params)


def startRecord():
    """
    Starts the record output.
    
    
    """
    params = {}
    
    return __createMessage("StartRecord", params)


def stopRecord():
    """
    Stops the record output.
    
    
    """
    params = {}
    
    return __createMessage("StopRecord", params)


def toggleRecordPause():
    """
    Toggles pause on the record output.
    
    
    """
    params = {}
    
    return __createMessage("ToggleRecordPause", params)


def pauseRecord():
    """
    Pauses the record output.
    
    
    """
    params = {}
    
    return __createMessage("PauseRecord", params)


def resumeRecord():
    """
    Resumes the record output.
    
    
    """
    params = {}
    
    return __createMessage("ResumeRecord", params)


#endregion

#region SCENE ITEMS
def getSceneItemList(sceneName: str):
    """
    Gets a list of all scene items in a scene.
    
    Scenes only
    
    :param sceneName: String - Name of the scene to get the items of
    
    """
    params = {}
    params['sceneName'] = sceneName
    
    return __createMessage("GetSceneItemList", params)


def getGroupSceneItemList(sceneName: str):
    """
    Basically GetSceneItemList, but for groups.
    
    Using groups at all in OBS is discouraged, as they are very broken under the hood. Please use nested scenes instead.
    
    Groups only
    
    :param sceneName: String - Name of the group to get the items of
    
    """
    params = {}
    params['sceneName'] = sceneName
    
    return __createMessage("GetGroupSceneItemList", params)


def getSceneItemId(sceneName: str, sourceName: str, searchOffset: Optional[Union[int, float]] = None):
    """
    Searches a scene for a source, and returns its id.
    
    Scenes and Groups
    
    :param sceneName: String - Name of the scene or group to search in
    :param sourceName: String - Name of the source to find
    :param searchOffset: Number (Optional) - Number of matches to skip during search. >= 0 means first forward. -1 means last (top) item	Restrictions: >= -1	Optional Behaviour: 0
    
    """
    params = {}
    params['sceneName'] = sceneName
    params['sourceName'] = sourceName
    if searchOffset is not None:
        params['searchOffset'] = searchOffset
    
    return __createMessage("GetSceneItemId", params)


def createSceneItem(sceneName: str, sourceName: str, sceneItemEnabled: Optional[bool] = None):
    """
    Creates a new scene item using a source.
    
    Scenes only
    
    :param sceneName: String - Name of the scene to create the new item in
    :param sourceName: String - Name of the source to add to the scene
    :param sceneItemEnabled: Boolean (Optional) - Enable state to apply to the scene item on creation	Optional Behaviour: True
    
    """
    params = {}
    params['sceneName'] = sceneName
    params['sourceName'] = sourceName
    if sceneItemEnabled is not None:
        params['sceneItemEnabled'] = sceneItemEnabled
    
    return __createMessage("CreateSceneItem", params)


def removeSceneItem(sceneName: str, sceneItemId: Union[int, float]):
    """
    Removes a scene item from a scene.
    
    Scenes only
    
    :param sceneName: String - Name of the scene the item is in
    :param sceneItemId: Number - Numeric ID of the scene item	Restrictions: >= 0
    
    """
    params = {}
    params['sceneName'] = sceneName
    params['sceneItemId'] = sceneItemId
    
    return __createMessage("RemoveSceneItem", params)


def duplicateSceneItem(sceneName: str, sceneItemId: Union[int, float], destinationSceneName: Optional[str] = None):
    """
    Duplicates a scene item, copying all transform and crop info.
    
    Scenes only
    
    :param sceneName: String - Name of the scene the item is in
    :param sceneItemId: Number - Numeric ID of the scene item	Restrictions: >= 0
    :param destinationSceneName: String (Optional) - Name of the scene to create the duplicated item in	Optional Behaviour: 'sceneName' is assumed
    
    """
    params = {}
    params['sceneName'] = sceneName
    params['sceneItemId'] = sceneItemId
    if destinationSceneName is not None:
        params['destinationSceneName'] = destinationSceneName
    
    return __createMessage("DuplicateSceneItem", params)


def getSceneItemTransform(sceneName: str, sceneItemId: Union[int, float]):
    """
    Gets the transform and crop info of a scene item.
    
    Scenes and Groups
    
    :param sceneName: String - Name of the scene the item is in
    :param sceneItemId: Number - Numeric ID of the scene item	Restrictions: >= 0
    
    """
    params = {}
    params['sceneName'] = sceneName
    params['sceneItemId'] = sceneItemId
    
    return __createMessage("GetSceneItemTransform", params)


def setSceneItemTransform(sceneName: str, sceneItemId: Union[int, float], sceneItemTransform: Object):
    """
    Sets the transform and crop info of a scene item.
    
    :param sceneName: String - Name of the scene the item is in
    :param sceneItemId: Number - Numeric ID of the scene item	Restrictions: >= 0
    :param sceneItemTransform: Object - Object containing scene item transform info to update
    
    """
    params = {}
    params['sceneName'] = sceneName
    params['sceneItemId'] = sceneItemId
    params['sceneItemTransform'] = sceneItemTransform
    
    return __createMessage("SetSceneItemTransform", params)


def getSceneItemEnabled(sceneName: str, sceneItemId: Union[int, float]):
    """
    Gets the enable state of a scene item.
    
    Scenes and Groups
    
    :param sceneName: String - Name of the scene the item is in
    :param sceneItemId: Number - Numeric ID of the scene item	Restrictions: >= 0
    
    """
    params = {}
    params['sceneName'] = sceneName
    params['sceneItemId'] = sceneItemId
    
    return __createMessage("GetSceneItemEnabled", params)


def setSceneItemEnabled(sceneName: str, sceneItemId: Union[int, float], sceneItemEnabled: bool):
    """
    Sets the enable state of a scene item.
    
    Scenes and Groups
    
    :param sceneName: String - Name of the scene the item is in
    :param sceneItemId: Number - Numeric ID of the scene item	Restrictions: >= 0
    :param sceneItemEnabled: Boolean - New enable state of the scene item
    
    """
    params = {}
    params['sceneName'] = sceneName
    params['sceneItemId'] = sceneItemId
    params['sceneItemEnabled'] = sceneItemEnabled
    
    return __createMessage("SetSceneItemEnabled", params)


def getSceneItemLocked(sceneName: str, sceneItemId: Union[int, float]):
    """
    Gets the lock state of a scene item.
    
    Scenes and Groups
    
    :param sceneName: String - Name of the scene the item is in
    :param sceneItemId: Number - Numeric ID of the scene item	Restrictions: >= 0
    
    """
    params = {}
    params['sceneName'] = sceneName
    params['sceneItemId'] = sceneItemId
    
    return __createMessage("GetSceneItemLocked", params)


def setSceneItemLocked(sceneName: str, sceneItemId: Union[int, float], sceneItemLocked: bool):
    """
    Sets the lock state of a scene item.
    
    Scenes and Group
    
    :param sceneName: String - Name of the scene the item is in
    :param sceneItemId: Number - Numeric ID of the scene item	Restrictions: >= 0
    :param sceneItemLocked: Boolean - New lock state of the scene item
    
    """
    params = {}
    params['sceneName'] = sceneName
    params['sceneItemId'] = sceneItemId
    params['sceneItemLocked'] = sceneItemLocked
    
    return __createMessage("SetSceneItemLocked", params)


def getSceneItemIndex(sceneName: str, sceneItemId: Union[int, float]):
    """
    Gets the index position of a scene item in a scene.
    
    An index of 0 is at the bottom of the source list in the UI.
    
    Scenes and Groups
    
    :param sceneName: String - Name of the scene the item is in
    :param sceneItemId: Number - Numeric ID of the scene item	Restrictions: >= 0
    
    """
    params = {}
    params['sceneName'] = sceneName
    params['sceneItemId'] = sceneItemId
    
    return __createMessage("GetSceneItemIndex", params)


def setSceneItemIndex(sceneName: str, sceneItemId: Union[int, float], sceneItemIndex: Union[int, float]):
    """
    Sets the index position of a scene item in a scene.
    
    Scenes and Groups
    
    :param sceneName: String - Name of the scene the item is in
    :param sceneItemId: Number - Numeric ID of the scene item	Restrictions: >= 0
    :param sceneItemIndex: Number - New index position of the scene item	Restrictions: >= 0
    
    """
    params = {}
    params['sceneName'] = sceneName
    params['sceneItemId'] = sceneItemId
    params['sceneItemIndex'] = sceneItemIndex
    
    return __createMessage("SetSceneItemIndex", params)


def getSceneItemBlendMode(sceneName: str, sceneItemId: Union[int, float]):
    """
    Gets the blend mode of a scene item.
    
    Blend modes:
    
    - 'OBS_BLEND_NORMAL'
    - 'OBS_BLEND_ADDITIVE'
    - 'OBS_BLEND_SUBTRACT'
    - 'OBS_BLEND_SCREEN'
    - 'OBS_BLEND_MULTIPLY'
    - 'OBS_BLEND_LIGHTEN'
    - 'OBS_BLEND_DARKEN'
    
    Scenes and Groups
    
    :param sceneName: String - Name of the scene the item is in
    :param sceneItemId: Number - Numeric ID of the scene item	Restrictions: >= 0
    
    """
    params = {}
    params['sceneName'] = sceneName
    params['sceneItemId'] = sceneItemId
    
    return __createMessage("GetSceneItemBlendMode", params)


def setSceneItemBlendMode(sceneName: str, sceneItemId: Union[int, float], sceneItemBlendMode: str):
    """
    Sets the blend mode of a scene item.
    
    Scenes and Groups
    
    :param sceneName: String - Name of the scene the item is in
    :param sceneItemId: Number - Numeric ID of the scene item	Restrictions: >= 0
    :param sceneItemBlendMode: String - New blend mode
    
    """
    params = {}
    params['sceneName'] = sceneName
    params['sceneItemId'] = sceneItemId
    params['sceneItemBlendMode'] = sceneItemBlendMode
    
    return __createMessage("SetSceneItemBlendMode", params)


#endregion

#region SCENES
def getSceneList():
    """
    Gets an array of all scenes in OBS.
    
    
    """
    params = {}
    
    return __createMessage("GetSceneList", params)


def getGroupList():
    """
    Gets an array of all groups in OBS.
    
    Groups in OBS are actually scenes, but renamed and modified. In obs-websocket, we treat them as scenes where we can.
    
    
    """
    params = {}
    
    return __createMessage("GetGroupList", params)


def getCurrentProgramScene():
    """
    Gets the current program scene.
    
    
    """
    params = {}
    
    return __createMessage("GetCurrentProgramScene", params)


def setCurrentProgramScene(sceneName: str):
    """
    Sets the current program scene.
    
    :param sceneName: String - Scene to set as the current program scene
    
    """
    params = {}
    params['sceneName'] = sceneName
    
    return __createMessage("SetCurrentProgramScene", params)


def getCurrentPreviewScene():
    """
    Gets the current preview scene.
    
    Only available when studio mode is enabled.
    
    
    """
    params = {}
    
    return __createMessage("GetCurrentPreviewScene", params)


def setCurrentPreviewScene(sceneName: str):
    """
    Sets the current preview scene.
    
    Only available when studio mode is enabled.
    
    :param sceneName: String - Scene to set as the current preview scene
    
    """
    params = {}
    params['sceneName'] = sceneName
    
    return __createMessage("SetCurrentPreviewScene", params)


def createScene(sceneName: str):
    """
    Creates a new scene in OBS.
    
    :param sceneName: String - Name for the new scene
    
    """
    params = {}
    params['sceneName'] = sceneName
    
    return __createMessage("CreateScene", params)


def removeScene(sceneName: str):
    """
    Removes a scene from OBS.
    
    :param sceneName: String - Name of the scene to remove
    
    """
    params = {}
    params['sceneName'] = sceneName
    
    return __createMessage("RemoveScene", params)


def setSceneName(sceneName: str, newSceneName: str):
    """
    Sets the name of a scene (rename).
    
    :param sceneName: String - Name of the scene to be renamed
    :param newSceneName: String - New name for the scene
    
    """
    params = {}
    params['sceneName'] = sceneName
    params['newSceneName'] = newSceneName
    
    return __createMessage("SetSceneName", params)


def getSceneSceneTransitionOverride(sceneName: str):
    """
    Gets the scene transition overridden for a scene.
    
    :param sceneName: String - Name of the scene
    
    """
    params = {}
    params['sceneName'] = sceneName
    
    return __createMessage("GetSceneSceneTransitionOverride", params)


def setSceneSceneTransitionOverride(sceneName: str, transitionName: Optional[str] = None, transitionDuration: Optional[Union[int, float]] = None):
    """
    Gets the scene transition overridden for a scene.
    
    :param sceneName: String - Name of the scene
    :param transitionName: String (Optional) - Name of the scene transition to use as override. Specify 'null' to remove	Optional Behaviour: Unchanged
    :param transitionDuration: Number (Optional) - Duration to use for any overridden transition. Specify 'null' to remove	Restrictions: >= 50, <= 20000	Optional Behaviour: Unchanged
    
    """
    params = {}
    params['sceneName'] = sceneName
    if transitionName is not None:
        params['transitionName'] = transitionName
    if transitionDuration is not None:
        params['transitionDuration'] = transitionDuration
    
    return __createMessage("SetSceneSceneTransitionOverride", params)


#endregion

#region SOURCES
def getSourceActive(sourceName: str):
    """
    Gets the active and show state of a source.
    
    **Compatible with inputs and scenes.**
    
    :param sourceName: String - Name of the source to get the active state of
    
    """
    params = {}
    params['sourceName'] = sourceName
    
    return __createMessage("GetSourceActive", params)


def getSourceScreenshot(sourceName: str, imageFormat: str, imageWidth: Optional[Union[int, float]] = None, imageHeight: Optional[Union[int, float]] = None, imageCompressionQuality: Optional[Union[int, float]] = None):
    """
    Gets a Base64-encoded screenshot of a source.
    
    The 'imageWidth' and 'imageHeight' parameters are treated as "scale to inner", meaning the smallest ratio will be used and the aspect ratio of the original resolution is kept.
    If 'imageWidth' and 'imageHeight' are not specified, the compressed image will use the full resolution of the source.
    
    **Compatible with inputs and scenes.**
    
    :param sourceName: String - Name of the source to take a screenshot of
    :param imageFormat: String - Image compression format to use. Use 'GetVersion' to get compatible image formats
    :param imageWidth: Number (Optional) - Width to scale the screenshot to	Restrictions: >= 8, <= 4096	Optional Behaviour: Source value is used
    :param imageHeight: Number (Optional) - Height to scale the screenshot to	Restrictions: >= 8, <= 4096	Optional Behaviour: Source value is used
    :param imageCompressionQuality: Number (Optional) - Compression quality to use. 0 for high compression, 100 for uncompressed. -1 to use "default" (whatever that means, idk)	Restrictions: >= -1, <= 100	Optional Behaviour: -1
    
    """
    params = {}
    params['sourceName'] = sourceName
    params['imageFormat'] = imageFormat
    if imageWidth is not None:
        params['imageWidth'] = imageWidth
    if imageHeight is not None:
        params['imageHeight'] = imageHeight
    if imageCompressionQuality is not None:
        params['imageCompressionQuality'] = imageCompressionQuality
    
    return __createMessage("GetSourceScreenshot", params)


#def saveSourceScreenshot(sourceName: str, imageFormat: str, imageFilePath: str, imageWidth: Optional[Union[int, float]] = None, imageHeight: Optional[Union[int, float]] = None, imageCompressionQuality: Optional[Union[int, float]] = None):
#    """
#    Saves a screenshot of a source to the filesystem.
#
#    The 'imageWidth' and 'imageHeight' parameters are treated as "scale to inner", meaning the smallest ratio will be used and the aspect ratio of the original resolution is kept.
#    If 'imageWidth' and 'imageHeight' are not specified, the compressed image will use the full resolution of the source.
#
#    **Compatible with inputs and scenes.**
#
#    :param sourceName: String - Name of the source to take a screenshot of
#    :param imageFormat: String - Image compression format to use. Use 'GetVersion' to get compatible image formats
#    :param imageFilePath: String - Path to save the screenshot file to. Eg. 'C:\Users\user\Desktop\screenshot.png'
#    :param imageWidth: Number (Optional) - Width to scale the screenshot to	Restrictions: >= 8, <= 4096	Optional Behaviour: Source value is used
#    :param imageHeight: Number (Optional) - Height to scale the screenshot to	Restrictions: >= 8, <= 4096	Optional Behaviour: Source value is used
#    :param imageCompressionQuality: Number (Optional) - Compression quality to use. 0 for high compression, 100 for uncompressed. -1 to use "default" (whatever that means, idk)	Restrictions: >= -1, <= 100	Optional Behaviour: -1
#
#    """
#    params = {}
#    params['sourceName'] = sourceName
#    params['imageFormat'] = imageFormat
#    params['imageFilePath'] = imageFilePath
#    if imageWidth is not None:
#        params['imageWidth'] = imageWidth
#    if imageHeight is not None:
#        params['imageHeight'] = imageHeight
#    if imageCompressionQuality is not None:
#        params['imageCompressionQuality'] = imageCompressionQuality
    
#    return __createMessage("SaveSourceScreenshot", params)


#endregion

#region STREAM
def getStreamStatus():
    """
    Gets the status of the stream output.
    
    
    """
    params = {}
    
    return __createMessage("GetStreamStatus", params)


def toggleStream():
    """
    Toggles the status of the stream output.
    
    
    """
    params = {}
    
    return __createMessage("ToggleStream", params)


def startStream():
    """
    Starts the stream output.
    
    
    """
    params = {}
    
    return __createMessage("StartStream", params)


def stopStream():
    """
    Stops the stream output.
    
    
    """
    params = {}
    
    return __createMessage("StopStream", params)


def sendStreamCaption(captionText: str):
    """
    Sends CEA-608 caption text over the stream output.
    
    :param captionText: String - Caption text
    
    """
    params = {}
    params['captionText'] = captionText
    
    return __createMessage("SendStreamCaption", params)


#endregion

#region TRANSITIONS
def getTransitionKindList():
    """
    Gets an array of all available transition kinds.
    
    Similar to 'GetInputKindList'
    
    
    """
    params = {}
    
    return __createMessage("GetTransitionKindList", params)


def getSceneTransitionList():
    """
    Gets an array of all scene transitions in OBS.
    
    
    """
    params = {}
    
    return __createMessage("GetSceneTransitionList", params)


def getCurrentSceneTransition():
    """
    Gets information about the current scene transition.
    
    
    """
    params = {}
    
    return __createMessage("GetCurrentSceneTransition", params)


def setCurrentSceneTransition(transitionName: str):
    """
    Sets the current scene transition.
    
    Small note: While the namespace of scene transitions is generally unique, that uniqueness is not a guarantee as it is with other resources like inputs.
    
    :param transitionName: String - Name of the transition to make active
    
    """
    params = {}
    params['transitionName'] = transitionName
    
    return __createMessage("SetCurrentSceneTransition", params)


def setCurrentSceneTransitionDuration(transitionDuration: Union[int, float]):
    """
    Sets the duration of the current scene transition, if it is not fixed.
    
    :param transitionDuration: Number - Duration in milliseconds	Restrictions: >= 50, <= 20000
    
    """
    params = {}
    params['transitionDuration'] = transitionDuration
    
    return __createMessage("SetCurrentSceneTransitionDuration", params)


def setCurrentSceneTransitionSettings(transitionSettings: Object, overlay: Optional[bool] = None):
    """
    Sets the settings of the current scene transition.
    
    :param transitionSettings: Object - Settings object to apply to the transition. Can be '{}'
    :param overlay: Boolean (Optional) - Whether to overlay over the current settings or replace them	Optional Behaviour: true
    
    """
    params = {}
    params['transitionSettings'] = transitionSettings
    if overlay is not None:
        params['overlay'] = overlay
    
    return __createMessage("SetCurrentSceneTransitionSettings", params)


def getCurrentSceneTransitionCursor():
    """
    Gets the cursor position of the current scene transition.
    
    Note: 'transitionCursor' will return 1.0 when the transition is inactive.
    
    
    """
    params = {}
    
    return __createMessage("GetCurrentSceneTransitionCursor", params)


def triggerStudioModeTransition():
    """
    Triggers the current scene transition. Same functionality as the 'Transition' button in studio mode.
    
    
    """
    params = {}
    
    return __createMessage("TriggerStudioModeTransition", params)


def setTBarPosition(position: Union[int, float], release: Optional[bool] = None):
    """
    Sets the position of the TBar.
    
    **Very important note**: This will be deprecated and replaced in a future version of obs-websocket.
    
    :param position: Number - New position	Restrictions: >= 0.0, <= 1.0
    :param release: Boolean (Optional) - Whether to release the TBar. Only set 'false' if you know that you will be sending another position update	Optional Behaviour: 'true'
    
    """
    params = {}
    params['position'] = position
    if release is not None:
        params['release'] = release
    
    return __createMessage("SetTBarPosition", params)


#endregion

#region UI
def getStudioModeEnabled():
    """
    Gets whether studio is enabled.
    
    
    """
    params = {}
    
    return __createMessage("GetStudioModeEnabled", params)


def setStudioModeEnabled(studioModeEnabled: bool):
    """
    Enables or disables studio mode
    
    :param studioModeEnabled: Boolean - True == Enabled, False == Disabled
    
    """
    params = {}
    params['studioModeEnabled'] = studioModeEnabled
    
    return __createMessage("SetStudioModeEnabled", params)


def openInputPropertiesDialog(inputName: str):
    """
    Opens the properties dialog of an input.
    
    :param inputName: String - Name of the input to open the dialog of
    
    """
    params = {}
    params['inputName'] = inputName
    
    return __createMessage("OpenInputPropertiesDialog", params)


def openInputFiltersDialog(inputName: str):
    """
    Opens the filters dialog of an input.
    
    :param inputName: String - Name of the input to open the dialog of
    
    """
    params = {}
    params['inputName'] = inputName
    
    return __createMessage("OpenInputFiltersDialog", params)


def openInputInteractDialog(inputName: str):
    """
    Opens the interact dialog of an input.
    
    :param inputName: String - Name of the input to open the dialog of
    
    """
    params = {}
    params['inputName'] = inputName
    
    return __createMessage("OpenInputInteractDialog", params)


def getMonitorList():
    """
    Gets a list of connected monitors and information about them.
    
    
    """
    params = {}
    
    return __createMessage("GetMonitorList", params)


def openVideoMixProjector(videoMixType: str, monitorIndex: Optional[Union[int, float]] = None, projectorGeometry: Optional[str] = None):
    """
    Opens a projector for a specific output video mix.
    
    Mix types:
    
    - 'OBS_WEBSOCKET_VIDEO_MIX_TYPE_PREVIEW'
    - 'OBS_WEBSOCKET_VIDEO_MIX_TYPE_PROGRAM'
    - 'OBS_WEBSOCKET_VIDEO_MIX_TYPE_MULTIVIEW'
    
    Note: This request serves to provide feature parity with 4.x. It is very likely to be changed/deprecated in a future release.
    
    :param videoMixType: String - Type of mix to open
    :param monitorIndex: Number (Optional) - Monitor index, use 'GetMonitorList' to obtain index	Optional Behaviour: -1: Opens projector in windowed mode
    :param projectorGeometry: String (Optional) - Size/Position data for a windowed projector, in Qt Base64 encoded format. Mutually exclusive with 'monitorIndex'	Optional Behaviour: N/A
    
    """
    params = {}
    params['videoMixType'] = videoMixType
    if monitorIndex is not None:
        params['monitorIndex'] = monitorIndex
    if projectorGeometry is not None:
        params['projectorGeometry'] = projectorGeometry
    
    return __createMessage("OpenVideoMixProjector", params)


def openSourceProjector(sourceName: str, monitorIndex: Optional[Union[int, float]] = None, projectorGeometry: Optional[str] = None):
    """
    Opens a projector for a source.
    
    Note: This request serves to provide feature parity with 4.x. It is very likely to be changed/deprecated in a future release.
    
    :param sourceName: String - Name of the source to open a projector for
    :param monitorIndex: Number (Optional) - Monitor index, use 'GetMonitorList' to obtain index	Optional Behaviour: -1: Opens projector in windowed mode
    :param projectorGeometry: String (Optional) - Size/Position data for a windowed projector, in Qt Base64 encoded format. Mutually exclusive with 'monitorIndex'	Optional Behaviour: N/A
    
    """
    params = {}
    params['sourceName'] = sourceName
    if monitorIndex is not None:
        params['monitorIndex'] = monitorIndex
    if projectorGeometry is not None:
        params['projectorGeometry'] = projectorGeometry
    
    return __createMessage("OpenSourceProjector", params)


#endregion

