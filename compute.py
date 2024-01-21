from .generate_nodes import *
import os
import bpy


def clean_animation(context):
    scene = context.scene
    try:
        fcurves = scene.animation_data.action.fcurves

        i = 0
        while i < len(fcurves):
            if fcurves[i].data_path.startswith("audio_volume_nodes"):
                fcurves.remove(fcurves[i])
                i -= 1
            i += 1
    except:
        pass


class RunAnalysis(bpy.types.Operator):
    bl_idname = "audio_volume_nodes.run_analysis"
    bl_label = "Analyze Audio"
    bl_description = "Run analysis of audio file"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        # get fps from scene and properties
        fps = context.scene.render.fps
        properties = context.scene.audio_volume_nodes

        if len(properties.audio_sources) == 0:
            self.report({'ERROR'}, "No audio files selected")
            return {'CANCELLED'}

        if len(properties.audio_sources) > 6:
            self.report({'ERROR'}, "Too many open files, can only support 6")
            return {'CANCELLED'}

        clean_animation(context)

        import librosa
        import numpy as np

        waves = []
        loudness_id = 4
        for audio in properties.audio_sources:
            wave = os.path.basename(audio.name)
            y, sr = librosa.load(audio.name)
            loudness = librosa.feature.melspectrogram(y=y, sr=sr, hop_length=int(sr / fps), n_mels=1)[0]
            loudness /= np.amax(loudness)

            for i in range(len(loudness)):
                s_loudness_id = "loudness_%s" % loudness_id
                setattr(properties, s_loudness_id, loudness[i])
                properties.keyframe_insert(data_path=s_loudness_id,
                                           frame=i + properties.frame_offset,
                                           group="Audio Volume Nodes")
            waves.append(wave)
            loudness_id += 1

        # generate / refresh nodes
        generate_sound_basic(waves)

        return {'FINISHED'}
