import bpy
from bpy.props import *

class MoonRayPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        layout = self.layout
        col = layout.column()

def get_user_prefs(context=None):
    if not context:
        context = bpy.context

    if hasattr(context, "user_preferences"):
        prefs = context.user_preferences.addons[__package__]
    elif hasattr(context, "preferences"):
        prefs = context.preferences.addons[__package__]
    if prefs:
        return prefs.preferences
    return None

class MoonRayConfig(bpy.types.PropertyGroup):
    
    devices = [
        ("CPU", "CPU", "Use CPU", 0),
        ("GPU", "GPU", "Use GPU", 1)
    ]

    device: EnumProperty(name="Device", items=devices, default="CPU")

class MoonRayScene(bpy.types.PropertyGroup):
    config: PointerProperty(type=MoonRayConfig)

    @classmethod
    def register(cls):
        bpy.types.Scene.moonray = PointerProperty(
            name="MoonRay Scene Settings",
            description="MoonRay scene settings",
            type=cls,
        )

    @classmethod
    def unregister(cls):
        del bpy.types.Scene.moonray

classes = [MoonRayPreferences, MoonRayConfig, MoonRayScene]