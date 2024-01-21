bl_info = {
    "name": "Audio Volume Nodes",
    "version": (1, 1, 0),
    "blender": (4, 0, 0),
    "location": "Geometry Nodes",
    "warning": "",
    "wiki_url": "",
    "category": "Geometry",
    "bl_options": {"REGISTER", "UNDO"}}

import importlib
import sys
import bpy

from .preferences import *
from .ui import *
from .properties import *
from .load_audio import *
from .compute import RunAnalysis


def register():
    # preferences
    bpy.utils.register_class(InstallDependencies)
    bpy.utils.register_class(UninstallDepencencies)
    bpy.utils.register_class(CheckInstallation)
    bpy.utils.register_class(Preferences)

    # properties
    bpy.utils.register_class(AudioVolumeNodesPropertyGroup)
    bpy.types.Scene.audio_volume_nodes = bpy.props.PointerProperty(type=AudioVolumeNodesPropertyGroup)

    # operators
    bpy.utils.register_class(LoadAudio)
    bpy.utils.register_class(RunAnalysis)

    # ui
    bpy.utils.register_class(AUDIOVOLUMENODES_PT_Panel)


def unregister():
    # preferences
    bpy.utils.unregister_class(Preferences)
    bpy.utils.unregister_class(InstallDependencies)
    bpy.utils.unregister_class(UninstallDepencencies)
    bpy.utils.unregister_class(CheckInstallation)

    # properties
    bpy.utils.unregister_class(AudioVolumeNodesPropertyGroup)

    # operators
    bpy.utils.unregister_class(LoadAudio)
    bpy.utils.unregister_class(RunAnalysis)

    # ui
    bpy.utils.unregister_class(AUDIOVOLUMENODES_PT_Panel)



if __name__ == '__main__':
    register()