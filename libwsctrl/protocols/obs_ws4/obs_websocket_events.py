

#region SCENES
EVENT_SWITCHSCENES: str = 'SwitchScenes'
"""Indicates a scene change."""

EVENT_SCENESCHANGED: str = 'ScenesChanged'
"""The scene list has been modified. Scenes have been added, removed, or renamed.

*Note: This event is not fired when the scenes are reordered.*"""

EVENT_SCENECOLLECTIONCHANGED: str = 'SceneCollectionChanged'
"""Triggered when switching to another scene collection or when renaming the current scene collection."""

EVENT_SCENECOLLECTIONLISTCHANGED: str = 'SceneCollectionListChanged'
"""Triggered when a scene collection is created, added, renamed, or removed."""

#endregion

#region TRANSITIONS
EVENT_SWITCHTRANSITION: str = 'SwitchTransition'
"""The active transition has been changed."""

EVENT_TRANSITIONLISTCHANGED: str = 'TransitionListChanged'
"""The list of available transitions has been modified.
Transitions have been added, removed, or renamed."""

EVENT_TRANSITIONDURATIONCHANGED: str = 'TransitionDurationChanged'
"""The active transition duration has been changed."""

EVENT_TRANSITIONBEGIN: str = 'TransitionBegin'
"""A transition (other than "cut") has begun."""

EVENT_TRANSITIONEND: str = 'TransitionEnd'
"""A transition (other than "cut") has ended.
Note: The `from-scene` field is not available in TransitionEnd."""

EVENT_TRANSITIONVIDEOEND: str = 'TransitionVideoEnd'
"""A stinger transition has finished playing its video."""

#endregion

#region PROFILES
EVENT_PROFILECHANGED: str = 'ProfileChanged'
"""Triggered when switching to another profile or when renaming the current profile."""

EVENT_PROFILELISTCHANGED: str = 'ProfileListChanged'
"""Triggered when a profile is created, added, renamed, or removed."""

#endregion

#region STREAMING
EVENT_STREAMSTARTING: str = 'StreamStarting'
"""A request to start streaming has been issued."""

EVENT_STREAMSTARTED: str = 'StreamStarted'
"""Streaming started successfully."""

EVENT_STREAMSTOPPING: str = 'StreamStopping'
"""A request to stop streaming has been issued."""

EVENT_STREAMSTOPPED: str = 'StreamStopped'
"""Streaming stopped successfully."""

EVENT_STREAMSTATUS: str = 'StreamStatus'
"""Emitted every 2 seconds when stream is active."""

#endregion

#region RECORDING
EVENT_RECORDINGSTARTING: str = 'RecordingStarting'
"""A request to start recording has been issued.

*Note: `recordingFilename` is not provided in this event because this information
is not available at the time this event is emitted.*"""

EVENT_RECORDINGSTARTED: str = 'RecordingStarted'
"""Recording started successfully."""

EVENT_RECORDINGSTOPPING: str = 'RecordingStopping'
"""A request to stop recording has been issued."""

EVENT_RECORDINGSTOPPED: str = 'RecordingStopped'
"""Recording stopped successfully."""

EVENT_RECORDINGPAUSED: str = 'RecordingPaused'
"""Current recording paused"""

EVENT_RECORDINGRESUMED: str = 'RecordingResumed'
"""Current recording resumed"""

#endregion

#region VIRTUAL CAM
EVENT_VIRTUALCAMSTARTED: str = 'VirtualCamStarted'
"""Virtual cam started successfully."""

EVENT_VIRTUALCAMSTOPPED: str = 'VirtualCamStopped'
"""Virtual cam stopped successfully."""

#endregion

#region REPLAY BUFFER
EVENT_REPLAYSTARTING: str = 'ReplayStarting'
"""A request to start the replay buffer has been issued."""

EVENT_REPLAYSTARTED: str = 'ReplayStarted'
"""Replay Buffer started successfully"""

EVENT_REPLAYSTOPPING: str = 'ReplayStopping'
"""A request to stop the replay buffer has been issued."""

EVENT_REPLAYSTOPPED: str = 'ReplayStopped'
"""Replay Buffer stopped successfully"""

#endregion

#region OTHER
EVENT_EXITING: str = 'Exiting'
"""OBS is exiting."""

#endregion

#region GENERAL
EVENT_HEARTBEAT: str = 'Heartbeat'
"""Emitted every 2 seconds after enabling it by calling SetHeartbeat."""

EVENT_BROADCASTCUSTOMMESSAGE: str = 'BroadcastCustomMessage'
"""A custom broadcast message, sent by the server, requested by one of the websocket clients."""

#endregion

#region SOURCES
EVENT_SOURCECREATED: str = 'SourceCreated'
"""A source has been created. A source can be an input, a scene or a transition."""

EVENT_SOURCEDESTROYED: str = 'SourceDestroyed'
"""A source has been destroyed/removed. A source can be an input, a scene or a transition."""

EVENT_SOURCEVOLUMECHANGED: str = 'SourceVolumeChanged'
"""The volume of a source has changed."""

EVENT_SOURCEMUTESTATECHANGED: str = 'SourceMuteStateChanged'
"""A source has been muted or unmuted."""

EVENT_SOURCEAUDIODEACTIVATED: str = 'SourceAudioDeactivated'
"""A source has removed audio."""

EVENT_SOURCEAUDIOACTIVATED: str = 'SourceAudioActivated'
"""A source has added audio."""

EVENT_SOURCEAUDIOSYNCOFFSETCHANGED: str = 'SourceAudioSyncOffsetChanged'
"""The audio sync offset of a source has changed."""

EVENT_SOURCEAUDIOMIXERSCHANGED: str = 'SourceAudioMixersChanged'
"""Audio mixer routing changed on a source."""

EVENT_SOURCERENAMED: str = 'SourceRenamed'
"""A source has been renamed."""

EVENT_SOURCEFILTERADDED: str = 'SourceFilterAdded'
"""A filter was added to a source."""

EVENT_SOURCEFILTERREMOVED: str = 'SourceFilterRemoved'
"""A filter was removed from a source."""

EVENT_SOURCEFILTERVISIBILITYCHANGED: str = 'SourceFilterVisibilityChanged'
"""The visibility/enabled state of a filter changed"""

EVENT_SOURCEFILTERSREORDERED: str = 'SourceFiltersReordered'
"""Filters in a source have been reordered."""

#endregion

#region MEDIA
EVENT_MEDIAPLAYING: str = 'MediaPlaying'
"""A media source has started playing.

*Note: This event is only emitted when something actively controls the media/VLC source. In other words, the source will never emit this on its own naturally.*"""

EVENT_MEDIAPAUSED: str = 'MediaPaused'
"""A media source has been paused.

*Note: This event is only emitted when something actively controls the media/VLC source. In other words, the source will never emit this on its own naturally.*"""

EVENT_MEDIARESTARTED: str = 'MediaRestarted'
"""A media source has been restarted.

*Note: This event is only emitted when something actively controls the media/VLC source. In other words, the source will never emit this on its own naturally.*"""

EVENT_MEDIASTOPPED: str = 'MediaStopped'
"""A media source has been stopped.

*Note: This event is only emitted when something actively controls the media/VLC source. In other words, the source will never emit this on its own naturally.*"""

EVENT_MEDIANEXT: str = 'MediaNext'
"""A media source has gone to the next item in the playlist.

*Note: This event is only emitted when something actively controls the media/VLC source. In other words, the source will never emit this on its own naturally.*"""

EVENT_MEDIAPREVIOUS: str = 'MediaPrevious'
"""A media source has gone to the previous item in the playlist.

*Note: This event is only emitted when something actively controls the media/VLC source. In other words, the source will never emit this on its own naturally.*"""

EVENT_MEDIASTARTED: str = 'MediaStarted'
"""A media source has been started.

*Note: These events are emitted by the OBS sources themselves. For example when the media file starts playing. The behavior depends on the type of media source being used.*"""

EVENT_MEDIAENDED: str = 'MediaEnded'
"""A media source has ended.

*Note: These events are emitted by the OBS sources themselves. For example when the media file ends. The behavior depends on the type of media source being used.*"""

#endregion

#region SCENE ITEMS
EVENT_SOURCEORDERCHANGED: str = 'SourceOrderChanged'
"""Scene items within a scene have been reordered."""

EVENT_SCENEITEMADDED: str = 'SceneItemAdded'
"""A scene item has been added to a scene."""

EVENT_SCENEITEMREMOVED: str = 'SceneItemRemoved'
"""A scene item has been removed from a scene."""

EVENT_SCENEITEMVISIBILITYCHANGED: str = 'SceneItemVisibilityChanged'
"""A scene item's visibility has been toggled."""

EVENT_SCENEITEMLOCKCHANGED: str = 'SceneItemLockChanged'
"""A scene item's locked status has been toggled."""

EVENT_SCENEITEMTRANSFORMCHANGED: str = 'SceneItemTransformChanged'
"""A scene item's transform has been changed."""

EVENT_SCENEITEMSELECTED: str = 'SceneItemSelected'
"""A scene item is selected."""

EVENT_SCENEITEMDESELECTED: str = 'SceneItemDeselected'
"""A scene item is deselected."""

#endregion

#region STUDIO MODE
EVENT_PREVIEWSCENECHANGED: str = 'PreviewSceneChanged'
"""The selected preview scene has changed (only available in Studio Mode)."""

EVENT_STUDIOMODESWITCHED: str = 'StudioModeSwitched'
"""Studio Mode has been enabled or disabled."""

#endregion

