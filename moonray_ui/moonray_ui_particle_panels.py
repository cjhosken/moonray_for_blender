from .moonray_ui_base import _MoonRayPanelHeader, ShaderPanel, ShaderNodePanel, CollectionPanel, MoonRayButtonsPanel
import bpy
from bpy.types import Panel

class PARTICLE_PT_moonray_hair(MoonRayButtonsPanel, Panel):
    bl_context = "particle"
    bl_label = "MoonRay Hair"

    @classmethod
    def poll(cls, context):
        psys = context.particle_system

        if psys is None or psys.settings is None:
            return False

        is_hair = psys.settings.type == "HAIR"
        is_path = psys.settings.render_type == "PATH"

        return context.scene.render.engine == "MOONRAY" and is_hair and is_path

    def draw(self, context):
        self.layout.use_property_split = True
        self.layout.use_property_decorate = False


classes = [PARTICLE_PT_moonray_hair]