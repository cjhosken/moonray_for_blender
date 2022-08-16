from bl_ui.properties_data_light import DataButtonsPanel
from .moonray_ui_base import _MoonRayPanelHeader, ShaderPanel, ShaderNodePanel, CollectionPanel, MoonRayButtonsPanel
import bpy
from bpy.types import Panel

class LIGHT_PT_moonray_light(DataButtonsPanel, Panel):
    COMPAT_ENGINES = {"MOONRAY"}
    bl_label = "MoonRay Light"
    bl_idname = "DATA_PT_light"
    bl_order = 1


    

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return context.light and engine == "MOONRAY"


    def draw(self, context):
        layout = self.layout

        light = context.light

        layout.row().prop(light, "type", expand=True)


classes = [LIGHT_PT_moonray_light]