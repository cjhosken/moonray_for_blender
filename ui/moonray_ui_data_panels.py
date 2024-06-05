import bpy
from .moonray_ui_base import MoonRayPanel


class LIGHT_PT_moonray_light(MoonRayPanel, bpy.types.Panel):
    bl_label = "MoonRay Light"
    bl_idname = "DATA_PT_light"
    bl_order = 1

    @classmethod
    def poll(cls, context):
        return MoonRayPanel.poll(context) and context.light

    def draw(self, context):
        layout = self.layout
        light = context.light
        layout.row().prop(light, "type", expand=True)

classes = [LIGHT_PT_moonray_light]