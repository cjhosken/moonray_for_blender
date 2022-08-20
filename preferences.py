import bpy
from bpy.types import AddonPreferences, PropertyGroup, Scene
from bpy.props import *

class PREFERENCES_PT_moonray_addon(AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        layout = self.layout
        col = layout.column()

class MoonRayPreferences(PropertyGroup):
    temp: BoolProperty()

class MoonRayConfig(PropertyGroup):
    
    devices = [
        ("CPU", "CPU", "Use CPU", 0),
        ("GPU", "GPU", "Use GPU", 1)
    ]

    device: EnumProperty(name="Device", items=devices, default="CPU")


class MoonRayScene(PropertyGroup):
    config: PointerProperty(type=MoonRayConfig)

    prefs: PointerProperty(type=MoonRayPreferences)

    @classmethod
    def register(cls):
        Scene.moonray = PointerProperty(
            name="MoonRay Scene Settings",
            description="MoonRay scene settings",
            type=cls,
        )

    @classmethod
    def unregister(cls):
        del Scene.moonray

classes = [MoonRayPreferences, MoonRayConfig, MoonRayScene, PREFERENCES_PT_moonray_addon]