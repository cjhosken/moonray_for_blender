import bpy
from .moonray_ui_base import MoonRayPanel

class VIEWLAYER_PT_moonray_aovs(MoonRayPanel, bpy.types.Panel):
    bl_context = "view_layer"
    bl_label = "MoonRay AOVs"

    def draw(self, context):
        layout = self.layout

classes = [VIEWLAYER_PT_moonray_aovs]