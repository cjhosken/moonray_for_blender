from .moonray_ui_base import _MoonRayPanelHeader, ShaderPanel, ShaderNodePanel, CollectionPanel, MoonRayButtonsPanel
import bpy
from bpy.types import Panel

class VIEWLAYER_PT_moonray_aovs(MoonRayButtonsPanel, Panel):
    bl_context = "view_layer"
    bl_label = "MoonRay AOVs"

    def draw(self, context):
        self.layout.use_property_split = True
        self.layout.use_property_decorate = False

classes = [VIEWLAYER_PT_moonray_aovs]