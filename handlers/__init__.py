import bpy

from ..engine import MoonRayRenderEngine

def add_moonray_output_to_materials(scene):
    if scene.render.engine == 'MOONRAY':  # Assuming 'MOONRAY' is the identifier for MoonRayRenderEngine
        # Add MoonRayShaderNode_Output for object materials
        for obj in bpy.data.objects:
            if obj.type == 'MESH' and obj.data.materials:
                for mat_slot in obj.material_slots:
                    mat = mat_slot.material
                    if not mat.use_nodes:
                        mat.use_nodes = True
                    node_tree = mat.node_tree
                    nodes = node_tree.nodes

                    # Check if a MoonRayShaderNode_Output already exists
                    if not any(node.bl_idname == 'MoonRayShaderNode_Output' for node in nodes):
                        output_node = nodes.new(type='MoonRayShaderNode_Output')
                        output_node.location = (400, 0)

        # Add MoonRayShaderNode_Output for world materials
        world = bpy.context.scene.world
        if world:
            if not world.use_nodes:
                world.use_nodes = True
            node_tree = world.node_tree
            nodes = node_tree.nodes

            # Check if a MoonRayShaderNode_Output already exists
            if not any(node.bl_idname == 'MoonRayWorldShaderNode_Output' for node in nodes):
                output_node = nodes.new(type='MoonRayWorldShaderNode_Output')
                output_node.location = (400, 0)



def register():
    bpy.app.handlers.depsgraph_update_post.append(add_moonray_output_to_materials)

def unregister():
    try:
        bpy.app.handlers.depsgraph_update_post.remove(add_moonray_output_to_materials)
    except:
        pass