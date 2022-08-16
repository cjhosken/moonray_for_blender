from .moonray_ui_base import _MoonRayPanelHeader, ShaderPanel, ShaderNodePanel, CollectionPanel, MoonRayButtonsPanel
import bpy
from bpy.types import Panel

class SCENE_PT_moonray_light_groups(MoonRayButtonsPanel, Panel):
    bl_context = "scene"
    bl_label = "MoonRay Light Groups"

    def draw(self, context):
        self.layout.use_property_split = True
        self.layout.use_property_decorate = False


classes = [SCENE_PT_moonray_light_groups]