from nodeitems_utils import register_node_categories, unregister_node_categories, NodeItem
from bpy.utils import register_class, unregister_class

from . import moonray_bl_nodes_sockets

from .moonray_bl_nodes_base import MoonRayShadingNode, MoonRayShaderNodeCategory
from .moonray_bl_nodes_output import MoonRayOutputNode


__MOONRAY_NODES_ALREADY_REGISTERED__ = False

classes = [MoonRayShadingNode, MoonRayOutputNode]

__MOONRAY_NODE_CATEGORIES__ = [
    MoonRayShaderNodeCategory("MOONRAY", "MoonRay", items=[
        NodeItem("MoonRay_OutputNode")
    ])
]


def register():
    moonray_bl_nodes_sockets.register()

    global __MOONRAY_NODES_ALREADY_REGISTERED__

    for cls in classes:
        register_class(cls)

    if not __MOONRAY_NODES_ALREADY_REGISTERED__:
        try:
            register_node_categories('MOONRAYSHADERNODES', __MOONRAY_NODE_CATEGORIES__)  
        except:
            unregister_node_categories('MOONRAYSHADERNODES')
            register_node_categories('MOONRAYSHADERNODES', __MOONRAY_NODE_CATEGORIES__)  
            __MOONRAY_NODES_ALREADY_REGISTERED__ = True  


def unregister():
    for cls in classes:
        unregister_class(cls)

        moonray_bl_nodes_sockets.unregister()

    try:
        unregister_node_categories('MOONRAYSHADERNODES')
    except:
        pass
    