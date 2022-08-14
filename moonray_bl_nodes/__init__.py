from nodeitems_utils import register_node_categories, unregister_node_categories, NodeItem
from bpy.utils import register_class, unregister_class

from . import moonray_bl_nodes_sockets

from .moonray_bl_nodes_base import MoonRayShadingNode, MoonRayShaderNodeCategory, MoonRayWorldNodeCategory, MoonRayLightNodeCategory
from .nodes.moonray_bl_nodes_output import MoonRayShaderOutputNode, MoonRayWorldOutputNode, MoonRayLightOutputNode


__MOONRAY_NODES_ALREADY_REGISTERED__ = False

classes = [MoonRayShaderOutputNode, MoonRayWorldOutputNode, MoonRayLightOutputNode]

__MOONRAY_NODE_CATEGORIES__ = [
    MoonRayShaderNodeCategory("MOONRAYSHADERS", "MoonRay", items=[
        NodeItem("MoonRay_ShaderOutputNode")
    ]),
    MoonRayWorldNodeCategory("MOONRAYWOLRDS", "MoonRay", items=[
        NodeItem("MoonRay_WorldOutputNode")
    ]),
    MoonRayLightNodeCategory("MOONRAYLIGHTS", "MoonRay", items=[
        NodeItem("MoonRay_LightOutputNode")
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
    