import bpy, os

bl_info = {
    "name" : "MoonRay For Blender",
    "author" : "Christopher Hosken",
    "version" : (1, 6, 0, 0),
    "blender" : (4, 2, 3),
    "description" : "Dreamworks' MoonRay Production Renderer integration into Blender",
    "warning" : "This Addon is currently under development",
    "support": "COMMUNITY",
    "doc_url": "https:bl//github.com/cjhosken/moonray_for_blender/wiki",
    "tracker_url": "https://github.com/cjhosken/moonray_for_blender/issues",
    "category" : "Render"
}

from . import properties, nodes, engine, ui, handlers, operators, mfb, preferences

def register():
    mfb.register()
    properties.register()
    preferences.register()
    engine.register()
    handlers.register()
    operators.register()
    nodes.register()
    ui.register()

def unregister():
    ui.unregister()
    nodes.unregister()
    operators.unregister()
    handlers.unregister()
    engine.unregister()
    preferences.unregister()
    properties.unregister()
    mfb.unregister()