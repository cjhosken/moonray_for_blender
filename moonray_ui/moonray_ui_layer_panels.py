from .moonray_ui_base import _MoonRayPanelHeader, ShaderPanel, ShaderNodePanel, CollectionPanel, MoonRayButtonsPanel
import bpy
from bpy.types import Panel

class MATERIAL_PT_moonray_aovs(MoonRayButtonsPanel, Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_options = {'DEFAULT_CLOSED'}
    bl_context = "view_layer"
    bl_label = "MoonRay AOVs"

    def draw(self, context):
        self.layout.use_property_split = True
        self.layout.use_property_decorate = False

        if context.scene.render.engine != "MOONRAY":
            return

classes = [MATERIAL_PT_moonray_aovs]