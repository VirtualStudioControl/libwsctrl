from enum import Enum


#region EventSubscription

class EventSubscription(Enum):

    NONE = 0
    """
    Subcription value used to disable all events.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    General = (1 << 0)
    """
    Subscription value to receive events in the `General` category.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    Config = (1 << 1)
    """
    Subscription value to receive events in the `Config` category.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    Scenes = (1 << 2)
    """
    Subscription value to receive events in the `Scenes` category.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    Inputs = (1 << 3)
    """
    Subscription value to receive events in the `Inputs` category.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    Transitions = (1 << 4)
    """
    Subscription value to receive events in the `Transitions` category.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    Filters = (1 << 5)
    """
    Subscription value to receive events in the `Filters` category.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    Outputs = (1 << 6)
    """
    Subscription value to receive events in the `Outputs` category.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    SceneItems = (1 << 7)
    """
    Subscription value to receive events in the `SceneItems` category.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    MediaInputs = (1 << 8)
    """
    Subscription value to receive events in the `MediaInputs` category.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    Vendors = (1 << 9)
    """
    Subscription value to receive the `VendorEvent` event.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    Ui = (1 << 10)
    """
    Subscription value to receive events in the `Ui` category.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    All = (General | Config | Scenes | Inputs | Transitions | Filters | Outputs | SceneItems | MediaInputs | Vendors | Ui)
    """
    Helper to receive all non-high-volume events.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    InputVolumeMeters = (1 << 16)
    """
    Subscription value to receive the `InputVolumeMeters` high-volume event.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    InputActiveStateChanged = (1 << 17)
    """
    Subscription value to receive the `InputActiveStateChanged` high-volume event.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    InputShowStateChanged = (1 << 18)
    """
    Subscription value to receive the `InputShowStateChanged` high-volume event.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    SceneItemTransformChanged = (1 << 19)
    """
    Subscription value to receive the `SceneItemTransformChanged` high-volume event.

    RPC Version: 1

    Initial Version: 5.0.0
    """


#endregion

#region RequestBatchExecutionType

class RequestBatchExecutionType(Enum):

    NONE = -1
    """
    Not a request batch.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    SerialRealtime = 0
    """
    A request batch which processes all requests serially, as fast as possible.
    
    Note: To introduce artificial delay, use the `Sleep` request and the `sleepMillis` request field.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    SerialFrame = 1
    """
    A request batch type which processes all requests serially, in sync with the graphics thread. Designed to provide high accuracy for animations.
    
    Note: To introduce artificial delay, use the `Sleep` request and the `sleepFrames` request field.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    Parallel = 2
    """
    A request batch type which processes all requests using all available threads in the thread pool.
    
    Note: This is mainly experimental, and only really shows its colors during requests which require lots of
    active processing, like `GetSourceScreenshot`.

    RPC Version: 1

    Initial Version: 5.0.0
    """


#endregion

#region RequestStatus

class RequestStatus(Enum):

    Unknown = 0
    """
    Unknown status, should never be used.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    NoError = 10
    """
    For internal use to signify a successful field check.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    Success = 100
    """
    The request has succeeded.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    MissingRequestType = 203
    """
    The `requestType` field is missing from the request data.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    UnknownRequestType = 204
    """
    The request type is invalid or does not exist.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    GenericError = 205
    """
    Generic error code.
    
    Note: A comment is required to be provided by obs-websocket.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    UnsupportedRequestBatchExecutionType = 206
    """
    The request batch execution type is not supported.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    MissingRequestField = 300
    """
    A required request field is missing.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    MissingRequestData = 301
    """
    The request does not have a valid requestData object.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    InvalidRequestField = 400
    """
    Generic invalid request field message.
    
    Note: A comment is required to be provided by obs-websocket.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    InvalidRequestFieldType = 401
    """
    A request field has the wrong data type.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    RequestFieldOutOfRange = 402
    """
    A request field (number) is outside of the allowed range.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    RequestFieldEmpty = 403
    """
    A request field (string or array) is empty and cannot be.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    TooManyRequestFields = 404
    """
    There are too many request fields (eg. a request takes two optionals, where only one is allowed at a time).

    RPC Version: 1

    Initial Version: 5.0.0
    """

    OutputRunning = 500
    """
    An output is running and cannot be in order to perform the request.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    OutputNotRunning = 501
    """
    An output is not running and should be.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    OutputPaused = 502
    """
    An output is paused and should not be.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    OutputNotPaused = 503
    """
    An output is not paused and should be.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    OutputDisabled = 504
    """
    An output is disabled and should not be.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    StudioModeActive = 505
    """
    Studio mode is active and cannot be.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    StudioModeNotActive = 506
    """
    Studio mode is not active and should be.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    ResourceNotFound = 600
    """
    The resource was not found.
    
    Note: Resources are any kind of object in obs-websocket, like inputs, profiles, outputs, etc.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    ResourceAlreadyExists = 601
    """
    The resource already exists.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    InvalidResourceType = 602
    """
    The type of resource found is invalid.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    NotEnoughResources = 603
    """
    There are not enough instances of the resource in order to perform the request.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    InvalidResourceState = 604
    """
    The state of the resource is invalid. For example, if the resource is blocked from being accessed.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    InvalidInputKind = 605
    """
    The specified input (obs_source_t-OBS_SOURCE_TYPE_INPUT) had the wrong kind.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    ResourceNotConfigurable = 606
    """
    The resource does not support being configured.
    
    This is particularly relevant to transitions, where they do not always have changeable settings.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    InvalidFilterKind = 607
    """
    The specified filter (obs_source_t-OBS_SOURCE_TYPE_FILTER) had the wrong kind.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    ResourceCreationFailed = 700
    """
    Creating the resource failed.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    ResourceActionFailed = 701
    """
    Performing an action on the resource failed.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    RequestProcessingFailed = 702
    """
    Processing the request failed unexpectedly.
    
    Note: A comment is required to be provided by obs-websocket.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    CannotAct = 703
    """
    The combination of request fields cannot be used to perform an action.

    RPC Version: 1

    Initial Version: 5.0.0
    """


#endregion

#region ObsMediaInputAction

class ObsMediaInputAction(Enum):
    pass
#    OBS_WEBSOCKET_MEDIA_INPUT_ACTION_NONE = OBS_WEBSOCKET_MEDIA_INPUT_ACTION_NONE # Deprecated
#    OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PLAY = OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PLAY # Deprecated
#    OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PAUSE = OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PAUSE # Deprecated
#    OBS_WEBSOCKET_MEDIA_INPUT_ACTION_STOP = OBS_WEBSOCKET_MEDIA_INPUT_ACTION_STOP # Deprecated
#    OBS_WEBSOCKET_MEDIA_INPUT_ACTION_RESTART = OBS_WEBSOCKET_MEDIA_INPUT_ACTION_RESTART # Deprecated
#    OBS_WEBSOCKET_MEDIA_INPUT_ACTION_NEXT = OBS_WEBSOCKET_MEDIA_INPUT_ACTION_NEXT # Deprecated
#    OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PREVIOUS = OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PREVIOUS # Deprecated

#endregion

#region WebSocketCloseCode

class WebSocketCloseCode(Enum):

    DontClose = 0
    """
    For internal use only to tell the request handler not to perform any close action.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    UnknownReason = 4000
    """
    Unknown reason, should never be used.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    MessageDecodeError = 4002
    """
    The server was unable to decode the incoming websocket message.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    MissingDataField = 4003
    """
    A data field is required but missing from the payload.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    InvalidDataFieldType = 4004
    """
    A data field's value type is invalid.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    InvalidDataFieldValue = 4005
    """
    A data field's value is invalid.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    UnknownOpCode = 4006
    """
    The specified `op` was invalid or missing.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    NotIdentified = 4007
    """
    The client sent a websocket message without first sending `Identify` message.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    AlreadyIdentified = 4008
    """
    The client sent an `Identify` message while already identified.
    
    Note: Once a client has identified, only `Reidentify` may be used to change session parameters.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    AuthenticationFailed = 4009
    """
    The authentication attempt (via `Identify`) failed.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    UnsupportedRpcVersion = 4010
    """
    The server detected the usage of an old version of the obs-websocket RPC protocol.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    SessionInvalidated = 4011
    """
    The websocket session has been invalidated by the obs-websocket server.
    
    Note: This is the code used by the `Kick` button in the UI Session List. If you receive this code, you must not automatically reconnect.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    UnsupportedFeature = 4012
    """
    A requested feature is not supported due to hardware/software limitations.

    RPC Version: 1

    Initial Version: 5.0.0
    """


#endregion

#region WebSocketOpCode

class WebSocketOpCode(Enum):

    Hello = 0
    """
    The initial message sent by obs-websocket to newly connected clients.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    Identify = 1
    """
    The message sent by a newly connected client to obs-websocket in response to a `Hello`.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    Identified = 2
    """
    The response sent by obs-websocket to a client after it has successfully identified with obs-websocket.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    Reidentify = 3
    """
    The message sent by an already-identified client to update identification parameters.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    Event = 5
    """
    The message sent by obs-websocket containing an event payload.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    Request = 6
    """
    The message sent by a client to obs-websocket to perform a request.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    RequestResponse = 7
    """
    The message sent by obs-websocket in response to a particular request from a client.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    RequestBatch = 8
    """
    The message sent by a client to obs-websocket to perform a batch of requests.

    RPC Version: 1

    Initial Version: 5.0.0
    """

    RequestBatchResponse = 9
    """
    The message sent by obs-websocket in response to a particular batch of requests from a client.

    RPC Version: 1

    Initial Version: 5.0.0
    """


#endregion

