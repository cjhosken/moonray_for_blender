import bpy
from .moonray_ui_base import MoonRayPanel


class RENDER_PT_moonray_render(MoonRayPanel, bpy.types.Panel):
    bl_context = "render"
    bl_label = "Render"

    def draw(self, context):
        layout = self.layout


class RENDER_PT_moonray_samples(MoonRayPanel, bpy.types.Panel):
    bl_context = "render"
    bl_label = "Samples"

    def draw(self, context):
        layout = self.layout


class RENDER_PT_moonray_motion_blur(MoonRayPanel, bpy.types.Panel):
    bl_context = "render"
    bl_label = "Motion Blur"

    def draw(self, context):
        layout = self.layout


classes = [RENDER_PT_moonray_render, RENDER_PT_moonray_samples, RENDER_PT_moonray_motion_blur]