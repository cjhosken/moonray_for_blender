import bpy

from . import mfb_node_menus

def register():
    mfb_node_menus.register()

def unregister():
    mfb_node_menus.unregister()