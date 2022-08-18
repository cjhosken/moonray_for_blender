import bpy
from .moonray_ui_base import MoonRayPanel


class MATERIAL_PT_moonray_world_preview(MoonRayPanel, bpy.types.Panel):
    bl_context = "world"
    bl_label = "Preview"

    @classmethod
    def poll(cls, context):
        if not MoonRayPanel.poll(context):
            return False   
            
        wor = getattr(context, 'world', None)
        if not wor:
            return False 
        return True

    def draw(self, context):
        layout = self.layout
        wor = context.world
        row = layout.row()

        if wor:
            row.template_preview(wor, show_buttons=1)


class MATERIAL_PT_moonray_world_surface(MoonRayPanel, bpy.types.Panel):
    bl_context = "world"
    bl_label = "MoonRay Surface"
    shader_type = 'World'

    def draw(self, context):
        pass

classes = [MATERIAL_PT_moonray_world_preview, MATERIAL_PT_moonray_world_surface]