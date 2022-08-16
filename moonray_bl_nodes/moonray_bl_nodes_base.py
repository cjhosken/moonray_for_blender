import bpy
from bpy.props import EnumProperty, StringProperty, CollectionProperty, BoolProperty, PointerProperty
from nodeitems_utils import NodeCategory

from ..preferences import get_user_prefs
from ..moonray_utils import shadergraph_utils

def get_color(node_type):
    type_id = ["output"].index(node_type)
    prefs = get_user_prefs()
    return [prefs.output_node_color][type_id]


class MoonRayShadingNode(bpy.types.ShaderNode):
    bl_label = 'MoonRay'
    moonray_node_type = 'output'

    @classmethod
    def poll(cls, ntree):
        rd = bpy.context.scene.render
        if rd.engine != 'MOONRAY':
            return False

        if hasattr(ntree, 'bl_idname'):
            return ntree.bl_idname == 'ShaderNodeTree'
        else:
            return True    
    
    def draw_buttons(self, context, layout):
        nt = self.id_data
        mat = context.material

    def update(self):
        for output in self.outputs:
            if not output.is_linked:
                continue
            if len(output.links) < 1:
                continue
            link = output.links[0]
            from_node_type = getattr(link.from_socket, 'moonray_type', None)
            to_node_type = getattr(link.to_socket, 'moonray_type', None)
            if not from_node_type:
                continue            
            if not to_node_type:
                continue

            if not shadergraph_utils.is_socket_same_type(link.from_socket, link.to_socket):
                node_tree = self.id_data
                try:
                    node_tree.links.remove(link)
                except:
                    pass
    
    def copy(self, node):
        pass

    def add_input(self, type, name, default=None, enabled=True):
        input = self.inputs.new(type, name)

        if hasattr(input, "default_value"):
            input.default_value = default

        input.enabled = enabled
        return input


class MoonRayShaderNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        rd = context.scene.render
        if (rd.engine != "MOONRAY"):
            return False
        return context.space_data.tree_type == "ShaderNodeTree" and context.space_data.shader_type in ["OBJECT"] and bpy.context.active_object.type != "LIGHT"

class MoonRayWorldNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        rd = context.scene.render
        if (rd.engine != "MOONRAY"):
            return False
        return context.space_data.tree_type == "ShaderNodeTree" and context.space_data.shader_type in ["WORLD"]

class MoonRayLightNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        rd = context.scene.render
        if (rd.engine != "MOONRAY"):
            return False
        return context.space_data.tree_type == "ShaderNodeTree" and context.space_data.shader_type in ["OBJECT"] and bpy.context.active_object.type == "LIGHT"