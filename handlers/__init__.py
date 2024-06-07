import bpy

from ..engine import MoonRayRenderEngine

def add_moonray_output_to_materials(scene):
    if scene.render.engine == MoonRayRenderEngine.bl_idname:
        for mat in bpy.data.materials:
            if not mat.use_nodes:
                mat.use_nodes = True
            node_tree = mat.node_tree
            nodes = node_tree.nodes

            # Check if a MoonRayShaderNode_Output already exists
            if not any(node.bl_idname == 'MoonRayShaderNode_Output' for node in nodes):
                output_node = nodes.new(type='MoonRayShaderNode_Output')
                output_node.location = (400, 0)


def register():
    bpy.app.handlers.depsgraph_update_post.append(add_moonray_output_to_materials)

def unregister():
    try:
        bpy.app.handlers.depsgraph_update_post.remove(add_moonray_output_to_materials)
    except:
        pass