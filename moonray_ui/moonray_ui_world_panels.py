from .moonray_ui_base import _MoonRayPanelHeader, ShaderPanel, ShaderNodePanel, CollectionPanel 
import bpy
from bpy.types import Panel

class MATERIAL_PT_moonray_world_preview(ShaderPanel, Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "world"
    bl_label = "Preview"

    @classmethod
    def poll(cls, context):
        if context.scene.render.engine != "MOONRAY":
            return        
        wor = getattr(context, 'world', None)
        if not wor:
            return False 
        return True

    def draw(self, context):
        layout = self.layout
        wor = context.world
        row = layout.row()

        if wor:
            row.template_preview(context.world, show_buttons=1)


class MATERIAL_PT_moonray_world_surface(ShaderPanel, Panel):
    bl_context = "world"
    bl_label = "Surface"
    shader_type = 'World'

    def draw(self, context):
        pass

classes = [MATERIAL_PT_moonray_world_preview, MATERIAL_PT_moonray_world_surface]