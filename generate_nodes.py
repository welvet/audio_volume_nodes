import bpy


def set_driver(node, path):
    driver = node.outputs[0].driver_add("default_value")
    driver.driver.expression = "var"

    var = driver.driver.variables.new()
    var.name = "var"
    var.targets[0].id_type = 'SCENE'
    var.targets[0].id = bpy.data.scenes['Scene']
    var.targets[0].data_path = path


def generate_sound_basic(waves):
    if "Audio Info" in bpy.data.node_groups:
        bpy.data.node_groups.remove("Audio Info")

    sound_basic = bpy.data.node_groups.new("Audio Info", "GeometryNodeTree")

    group_outputs = sound_basic.nodes.new('NodeGroupOutput')
    group_outputs.location = (300, 0)

    node_id = 0
    loudness_id = 4
    for wave in waves:
        output_label_name = "Loudness %s" % wave
        sound_basic.interface.new_socket(name=output_label_name, in_out='OUTPUT', socket_type='NodeSocketFloat')
        loudness = sound_basic.nodes.new('ShaderNodeValue')
        loudness.label = output_label_name
        loudness.location = (-200, node_id * 100)
        set_driver(loudness, "audio_volume_nodes[\"loudness_%s\"]" % loudness_id)

        sound_basic.links.new(loudness.outputs[0], group_outputs.inputs[output_label_name])
        node_id += 1
        loudness_id += 1

    frame = sound_basic.nodes.new('ShaderNodeValue')
    frame.label = 'Frame'
    frame.location = (-200, -200)
    driver = frame.outputs[0].driver_add("default_value")
    driver.driver.expression = "frame"
