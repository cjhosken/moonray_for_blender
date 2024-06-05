import bpy
from .moonray_ui_base import MoonRayPanel

class SCENE_PT_moonray_light_groups(MoonRayPanel, bpy.types.Panel):
    bl_context = "scene"
    bl_label = "MoonRay Light Groups"

    def draw(self, context):
        layout = self.layout


classes = [SCENE_PT_moonray_light_groups]