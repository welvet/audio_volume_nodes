import bpy

class AudioVolumeNodesPropertyGroup(bpy.types.PropertyGroup):
    audio_sources: bpy.props.CollectionProperty(
        type=bpy.types.OperatorFileListElement,
        description="Path to audio file"
    )

    frame_offset: bpy.props.IntProperty(
        description="Frame offset",
        default=1,
        min=0
    )

    loudness_4: bpy.props.FloatProperty(
        description="Loudness of audio 4",
        default=0.0,
        min=0.0,
        max=1.0
    )

    loudness_5: bpy.props.FloatProperty(
        description="Loudness of audio 5 ",
        default=0.0,
        min=0.0,
        max=1.0
    )

    loudness_6: bpy.props.FloatProperty(
        description="Loudness of audio 6",
        default=0.0,
        min=0.0,
        max=1.0
    )

    loudness_7: bpy.props.FloatProperty(
        description="Loudness of audio 7",
        default=0.0,
        min=0.0,
        max=1.0
    )

    loudness_8: bpy.props.FloatProperty(
        description="Loudness of audio 7",
        default=0.0,
        min=0.0,
        max=1.0
    )

    loudness_9: bpy.props.FloatProperty(
        description="Loudness of audio 7",
        default=0.0,
        min=0.0,
        max=1.0
    )