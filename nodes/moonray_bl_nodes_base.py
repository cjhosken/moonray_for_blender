import bpy
from bpy.props import FloatProperty, StringProperty
from bpy.types import Node, NodeSocket
from nodeitems_utils import NodeCategory, NodeItem, register_node_categories, unregister_node_categories
from .moonray_bl_nodes_sockets import socket_is_equal

from ..engine import MoonRayRenderEngine

class MoonRayShaderNode(Node):
    bl_idname = 'MoonRayShaderNodeType'
    bl_label = 'MoonRay Shader Node'
    
    my_float: FloatProperty(name="My Float", default=0.5)
    my_string: StringProperty(name="My String", default="Hello")
    
    def init(self, context):
        self.outputs.new('NodeSocketShader', "Shader")

    def draw_buttons(self, context, layout):
        layout.prop(self, "my_float")
        layout.prop(self, "my_string")

    def draw_label(self):
        return "Custom Shader Node"

class MoonRayCompNode(Node):
    bl_idname = 'MoonRayCompNodeType'
    bl_label = 'MoonRay Comp Node'

    @classmethod
    def poll(cls, ntree):
        rd = bpy.context.scene.render
        return rd.engine == MoonRayRenderEngine.bl_idname and ntree.bl_idname == "CompositorNodeTree"
    
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

# Define custom node categories
class MoonRayNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        rd = context.scene.render
        return rd.engine == MoonRayRenderEngine.bl_idname and context.space_data.tree_type == "ShaderNodeTree"

class MoonRayCompNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        rd = context.scene.render
        return rd.engine == MoonRayRenderEngine.bl_idname and context.space_data.tree_type == "CompositorNodeTree"
        
class MoonRayShaderNodeCategory(MoonRayNodeCategory):
    @classmethod
    def poll(cls, context):
        return MoonRayNodeCategory.poll(context) and context.space_data.shader_type == 'OBJECT' and context.active_object and context.active_object.type == 'MESH'

class MoonRayWorldNodeCategory(MoonRayNodeCategory):
    @classmethod
    def poll(cls, context):
        return MoonRayNodeCategory.poll(context) and context.space_data.shader_type == 'WORLD'

class MoonRayLightNodeCategory(MoonRayNodeCategory):
    @classmethod
    def poll(cls, context):
        return MoonRayNodeCategory.poll(context) and context.space_data.shader_type == 'OBJECT' and context.active_object and context.active_object.type == 'LIGHT'