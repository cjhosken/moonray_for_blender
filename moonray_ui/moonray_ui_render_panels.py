from .moonray_ui_base import _MoonRayPanelHeader, CollectionPanel, MoonRayButtonsPanel

from bpy.types import Panel
import bpy

class RENDER_PT_moonray_render(MoonRayButtonsPanel, Panel):
    bl_context = "render"
    bl_label = "Render"


    def draw(self, context):
        self.layout.use_property_split = True
        self.layout.use_property_decorate = False


class RENDER_PT_moonray_samples(MoonRayButtonsPanel, Panel):
    bl_context = "render"
    bl_label = "Samples"

    def draw(self, context):
        self.layout.use_property_split = True
        self.layout.use_property_decorate = False


class RENDER_PT_moonray_motion_blur(MoonRayButtonsPanel, Panel):
    bl_context = "render"
    bl_label = "Motion Blur"

    def draw(self, context):
        self.layout.use_property_split = True
        self.layout.use_property_decorate = False


classes = [RENDER_PT_moonray_render, RENDER_PT_moonray_samples, RENDER_PT_moonray_motion_blur]