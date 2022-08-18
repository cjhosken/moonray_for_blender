import bpy
from bpy.props import EnumProperty, StringProperty, CollectionProperty, BoolProperty, PointerProperty
from nodeitems_utils import NodeCategory

from .moonray_bl_nodes_sockets import socket_is_equal

from ..preferences import get_user_prefs

def get_color(node_type):
    type_id = ["output"].index(node_type)
    prefs = get_user_prefs()
    return [prefs.output_node_color][type_id]


class MoonRayShadingNode(bpy.types.ShaderNode):
    bl_label = 'MoonRayNode'

    @classmethod
    def poll(cls, ntree):
        rd = bpy.context.scene.render
        return rd.engine == "MOONRAY" and ntree.bl_idname == "ShaderNodeTree"
    
    def draw_buttons(self, context, layout):
        pass

    def update(self):
        for output in self.outputs:
            if not output.is_linked or len(output.links) < 1:
                continue

            link = output.links[0]

            from_node_type = getattr(link.from_socket, 'moonray_type', None)
            
            to_node_type = getattr(link.to_socket, 'moonray_type', None)

            if not from_node_type or not to_node_type:
                continue            

            if not socket_is_equal(link.from_socket, link.to_socket):
                node_tree = self.id_data
                node_tree.links.remove(link)
    
    def copy(self, node):
        pass

    def add_input(self, type, name, default=None, enabled=True):
        input = self.inputs.new(type, name)

        if hasattr(input, "default_value"):
            input.default_value = default

        input.enabled = enabled
        return input

class MoonRayNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        rd = context.scene.render
        return context.space_data.tree_type == "ShaderNodeTree" and rd.engine == "MOONRAY"

class MoonRayShaderNodeCategory(MoonRayNodeCategory):
    @classmethod
    def poll(cls, context):
        return MoonRayNodeCategory.poll(context) and context.space_data.shader_type in ["OBJECT"] and bpy.context.active_object.type in ["MESH"]

class MoonRayWorldNodeCategory(MoonRayNodeCategory):
    @classmethod
    def poll(cls, context):
        return  MoonRayNodeCategory.poll(context) and context.space_data.shader_type in ["WORLD"]

class MoonRayLightNodeCategory(MoonRayNodeCategory):
    @classmethod
    def poll(cls, context):
        return  MoonRayNodeCategory.poll(context) and context.space_data.shader_type in ["OBJECT"] and bpy.context.active_object.type in ["LIGHT"]