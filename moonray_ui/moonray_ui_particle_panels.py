import bpy
from .moonray_ui_base import MoonRayPanel


class PARTICLE_PT_moonray_hair(MoonRayPanel, bpy.types.Panel):
    bl_context = "particle"
    bl_label = "MoonRay Hair"

    @classmethod
    def poll(cls, context):
        psys = context.particle_system

        if psys is None or psys.settings is None:
            return False

        is_hair = psys.settings.type == "HAIR"
        is_path = psys.settings.render_type == "PATH"

        return MoonRayPanel.poll(context) and is_hair and is_path

    def draw(self, context):
        layout = self.layout


classes = [PARTICLE_PT_moonray_hair]