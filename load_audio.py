import bpy
from bpy.props import CollectionProperty, StringProperty
from bpy_extras.io_utils import ImportHelper
import os
from pathlib import Path

class LoadAudio(bpy.types.Operator, ImportHelper):
    bl_idname = "audio_volume_nodes.load_audio"
    bl_label = "Load Audio"
    bl_description = "Choose files from disk"
    bl_options = {'REGISTER', 'UNDO'}

    filter_glob: StringProperty(
        default='*.wav;*.mp3;*.ogg;*.flac',
        options={'HIDDEN'}
    )

    files: CollectionProperty(
        type=bpy.types.OperatorFileListElement,
        options={'HIDDEN'}
    )

    directory: StringProperty(subtype='DIR_PATH')

    def execute(self, context):
        if not context.scene.sequence_editor:
            context.scene.sequence_editor_create()

        context.scene.audio_volume_nodes.audio_sources.clear()

        for seq in context.scene.sequence_editor.sequences:
            if seq.name.endswith("- audio volume nodes"):
                context.scene.sequence_editor.sequences.remove(seq)

        channel_id = 4
        base = Path(self.directory)
        for file in self.files:
            filename = str(os.path.basename(file.name))
            new_name = filename[:40] + " - audio volume nodes"
            filepath = str(base / file.name)

            context.scene.sequence_editor.sequences.new_sound(name=new_name, filepath=filepath, frame_start=context.scene.audio_volume_nodes.frame_offset, channel=channel_id)
            channel_id += 1

            add = context.scene.audio_volume_nodes.audio_sources.add()
            add.name = filepath

        # set audio sync mode
        context.scene.sync_mode = 'AUDIO_SYNC'

        return {'FINISHED'}

