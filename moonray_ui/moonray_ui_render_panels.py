from .moonray_ui_base import _MoonRayPanelHeader, CollectionPanel, MoonRayButtonsPanel

from bpy.types import Panel
import bpy

class RENDER_PT_moonray_render(MoonRayButtonsPanel, Panel):
    bl_label = "Render"

    def draw(self, context):
        self.layout.use_property_split = True
        self.layout.use_property_decorate = False

        if context.scene.render.engine != "MOONRAY":
            return

        layout = self.layout

        row = layout.row(align=True)
        row.operator("render.render", text="Render")

        # Batch Render
        row.operator("render.render", text="Render Animation").animation = True

classes = [RENDER_PT_moonray_render]