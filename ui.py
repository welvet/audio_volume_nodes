import bpy

class AUDIOVOLUMENODES_PT_Panel(bpy.types.Panel):
    bl_idname = "AUDIOVOLUMENODES_PT_Panel"
    bl_label = "Audio Volume Nodes"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Audio Volume Nodes"
    bl_context = "object"

    def draw(self, context):
        propeties = context.scene.audio_volume_nodes

        layout = self.layout
        layout.label(text="Audio sources:")
        layout.operator("audio_volume_nodes.load_audio")
        layout.operator("audio_volume_nodes.run_analysis")

        box1 = layout.box()
        box1.label(text="Frame offset:")
        box1.prop(propeties, "frame_offset", text="Frame offset")
