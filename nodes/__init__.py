import bpy
from nodeitems_utils import register_node_categories, unregister_node_categories
from bpy.utils import register_class, unregister_class

from .moonray_bl_nodes_sockets import register_sockets
from .moonray_bl_nodes_sockets import socket_is_equal
from . import moonray_bl_nodes_sockets

from .moonray_bl_nodes_base import *

# Combine all node classes
from .nodes.light import classes as light_classes
from .nodes.shader import classes as shader_classes
from .nodes.world import classes as world_classes
from .nodes.comp import classes as comp_classes

classes = register_sockets() + shader_classes + light_classes + world_classes + comp_classes

register_classes, unregister_classes = bpy.utils.register_classes_factory((
    MoonRayShaderNode, MoonRayCompNode
))

node_categories = [
    MoonRayShaderNodeCategory("MOONRAYSHADERS", "MoonRay Shaders", items=[
        NodeItem("MoonrayShaderNodeType"),
    ]),
    MoonRayCompNodeCategory("MOONRAYCOMP", "MoonRay Comp", items=[
        NodeItem("MoonRayCompNodeType"),
    ]),
]

def register():
    register_classes()

    register_node_categories('MOONRAYSHADERNODES', node_categories)

def unregister():
    unregister_node_categories('MOONRAYSHADERNODES')

    unregister_classes()