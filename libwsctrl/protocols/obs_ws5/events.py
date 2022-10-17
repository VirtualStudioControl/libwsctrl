

#region CONFIG
EVENT_CURRENTSCENECOLLECTIONCHANGING: str = 'CurrentSceneCollectionChanging'
"""The current scene collection has begun changing.

Note: We recommend using this event to trigger a pause of all polling requests, as performing any requests during a
scene collection change is considered undefined behavior and can cause crashes!"""

EVENT_CURRENTSCENECOLLECTIONCHANGED: str = 'CurrentSceneCollectionChanged'
"""The current scene collection has changed.

Note: If polling has been paused during `CurrentSceneCollectionChanging`, this is the que to restart polling."""

EVENT_SCENECOLLECTIONLISTCHANGED: str = 'SceneCollectionListChanged'
"""The scene collection list has changed."""

EVENT_CURRENTPROFILECHANGING: str = 'CurrentProfileChanging'
"""The current profile has begun changing."""

EVENT_CURRENTPROFILECHANGED: str = 'CurrentProfileChanged'
"""The current profile has changed."""

EVENT_PROFILELISTCHANGED: str = 'ProfileListChanged'
"""The profile list has changed."""

#endregion

#region FILTERS
EVENT_SOURCEFILTERLISTREINDEXED: str = 'SourceFilterListReindexed'
"""A source's filter list has been reindexed."""

EVENT_SOURCEFILTERCREATED: str = 'SourceFilterCreated'
"""A filter has been added to a source."""

EVENT_SOURCEFILTERREMOVED: str = 'SourceFilterRemoved'
"""A filter has been removed from a source."""

EVENT_SOURCEFILTERNAMECHANGED: str = 'SourceFilterNameChanged'
"""The name of a source filter has changed."""

EVENT_SOURCEFILTERENABLESTATECHANGED: str = 'SourceFilterEnableStateChanged'
"""A source filter's enable state has changed."""

#endregion

#region GENERAL
EVENT_EXITSTARTED: str = 'ExitStarted'
"""OBS has begun the shutdown process."""

EVENT_VENDOREVENT: str = 'VendorEvent'
"""An event has been emitted from a vendor.

A vendor is a unique name registered by a third-party plugin or script, which allows for custom requests and events to be added to obs-websocket.
If a plugin or script implements vendor requests or events, documentation is expected to be provided with them."""

#endregion

#region INPUTS
EVENT_INPUTCREATED: str = 'InputCreated'
"""An input has been created."""

EVENT_INPUTREMOVED: str = 'InputRemoved'
"""An input has been removed."""

EVENT_INPUTNAMECHANGED: str = 'InputNameChanged'
"""The name of an input has changed."""

EVENT_INPUTACTIVESTATECHANGED: str = 'InputActiveStateChanged'
"""An input's active state has changed.

When an input is active, it means it's being shown by the program feed."""

EVENT_INPUTSHOWSTATECHANGED: str = 'InputShowStateChanged'
"""An input's show state has changed.

When an input is showing, it means it's being shown by the preview or a dialog."""

EVENT_INPUTMUTESTATECHANGED: str = 'InputMuteStateChanged'
"""An input's mute state has changed."""

EVENT_INPUTVOLUMECHANGED: str = 'InputVolumeChanged'
"""An input's volume level has changed."""

EVENT_INPUTAUDIOBALANCECHANGED: str = 'InputAudioBalanceChanged'
"""The audio balance value of an input has changed."""

EVENT_INPUTAUDIOSYNCOFFSETCHANGED: str = 'InputAudioSyncOffsetChanged'
"""The sync offset of an input has changed."""

EVENT_INPUTAUDIOTRACKSCHANGED: str = 'InputAudioTracksChanged'
"""The audio tracks of an input have changed."""

EVENT_INPUTAUDIOMONITORTYPECHANGED: str = 'InputAudioMonitorTypeChanged'
"""The monitor type of an input has changed.

Available types are:

- `OBS_MONITORING_TYPE_NONE`
- `OBS_MONITORING_TYPE_MONITOR_ONLY`
- `OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT`"""

EVENT_INPUTVOLUMEMETERS: str = 'InputVolumeMeters'
"""A high-volume event providing volume levels of all active inputs every 50 milliseconds."""

#endregion

#region MEDIA INPUTS
EVENT_MEDIAINPUTPLAYBACKSTARTED: str = 'MediaInputPlaybackStarted'
"""A media input has started playing."""

EVENT_MEDIAINPUTPLAYBACKENDED: str = 'MediaInputPlaybackEnded'
"""A media input has finished playing."""

EVENT_MEDIAINPUTACTIONTRIGGERED: str = 'MediaInputActionTriggered'
"""An action has been performed on an input."""

#endregion

#region OUTPUTS
EVENT_STREAMSTATECHANGED: str = 'StreamStateChanged'
"""The state of the stream output has changed."""

EVENT_RECORDSTATECHANGED: str = 'RecordStateChanged'
"""The state of the record output has changed."""

EVENT_REPLAYBUFFERSTATECHANGED: str = 'ReplayBufferStateChanged'
"""The state of the replay buffer output has changed."""

EVENT_VIRTUALCAMSTATECHANGED: str = 'VirtualcamStateChanged'
"""The state of the virtualcam output has changed."""

EVENT_REPLAYBUFFERSAVED: str = 'ReplayBufferSaved'
"""The replay buffer has been saved."""

#endregion

#region SCENE ITEMS
EVENT_SCENEITEMCREATED: str = 'SceneItemCreated'
"""A scene item has been created."""

EVENT_SCENEITEMREMOVED: str = 'SceneItemRemoved'
"""A scene item has been removed.

This event is not emitted when the scene the item is in is removed."""

EVENT_SCENEITEMLISTREINDEXED: str = 'SceneItemListReindexed'
"""A scene's item list has been reindexed."""

EVENT_SCENEITEMENABLESTATECHANGED: str = 'SceneItemEnableStateChanged'
"""A scene item's enable state has changed."""

EVENT_SCENEITEMLOCKSTATECHANGED: str = 'SceneItemLockStateChanged'
"""A scene item's lock state has changed."""

EVENT_SCENEITEMSELECTED: str = 'SceneItemSelected'
"""A scene item has been selected in the Ui."""

EVENT_SCENEITEMTRANSFORMCHANGED: str = 'SceneItemTransformChanged'
"""The transform/crop of a scene item has changed."""

#endregion

#region SCENES
EVENT_SCENECREATED: str = 'SceneCreated'
"""A new scene has been created."""

EVENT_SCENEREMOVED: str = 'SceneRemoved'
"""A scene has been removed."""

EVENT_SCENENAMECHANGED: str = 'SceneNameChanged'
"""The name of a scene has changed."""

EVENT_CURRENTPROGRAMSCENECHANGED: str = 'CurrentProgramSceneChanged'
"""The current program scene has changed."""

EVENT_CURRENTPREVIEWSCENECHANGED: str = 'CurrentPreviewSceneChanged'
"""The current preview scene has changed."""

EVENT_SCENELISTCHANGED: str = 'SceneListChanged'
"""The list of scenes has changed.

TODO: Make OBS fire this event when scenes are reordered."""

#endregion

#region TRANSITIONS
EVENT_CURRENTSCENETRANSITIONCHANGED: str = 'CurrentSceneTransitionChanged'
"""The current scene transition has changed."""

EVENT_CURRENTSCENETRANSITIONDURATIONCHANGED: str = 'CurrentSceneTransitionDurationChanged'
"""The current scene transition duration has changed."""

EVENT_SCENETRANSITIONSTARTED: str = 'SceneTransitionStarted'
"""A scene transition has started."""

EVENT_SCENETRANSITIONENDED: str = 'SceneTransitionEnded'
"""A scene transition has completed fully.

Note: Does not appear to trigger when the transition is interrupted by the user."""

EVENT_SCENETRANSITIONVIDEOENDED: str = 'SceneTransitionVideoEnded'
"""A scene transition's video has completed fully.

Useful for stinger transitions to tell when the video *actually* ends.
`SceneTransitionEnded` only signifies the cut point, not the completion of transition playback.

Note: Appears to be called by every transition, regardless of relevance."""

#endregion

#region UI
EVENT_STUDIOMODESTATECHANGED: str = 'StudioModeStateChanged'
"""Studio mode has been enabled or disabled."""

#endregion

