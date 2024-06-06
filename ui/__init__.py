import bpy

from .moonray_ui_material_panels import classes as ui_material_classes
from .moonray_ui_layer_panels import classes as ui_layer_classes
from .moonray_ui_world_panels import classes as ui_world_classes
from .moonray_ui_render_panels import classes as ui_render_classes
from .moonray_ui_scene_panels import classes as ui_scene_classes
from .moonray_ui_particle_panels import classes as ui_particle_classes
from .moonray_ui_data_panels import classes as ui_data_classes

from ..engine import MoonRayRenderEngine

classes = ui_material_classes + ui_render_classes + ui_world_classes + ui_layer_classes + ui_scene_classes + ui_particle_classes + ui_data_classes

register_classes, unregister_classes = bpy.utils.register_classes_factory(
    classes
)

def get_panels():
    exclude_panels = {
        'RENDER_PT_stamp',
        'DATA_PT_light',
        'DATA_PT_spot',
        'NODE_DATA_PT_light',
        'DATA_PT_falloff_curve',
        'RENDER_PT_post_processing',
        'RENDER_PT_simplify',
        'SCENE_PT_audio',
        'RENDER_PT_freestyle'
    }

    include_eevee_panels = {
        'MATERIAL_PT_preview',
        'EEVEE_MATERIAL_PT_context_material',
        'EEVEE_MATERIAL_PT_surface',
        'EEVEE_MATERIAL_PT_volume',
        'EEVEE_MATERIAL_PT_settings',
        'EEVEE_WORLD_PT_surface',
    }

    for panel_cls in bpy.types.Panel.__subclasses__():
        if hasattr(panel_cls, 'COMPAT_ENGINES') and (
            ('BLENDER_RENDER' in panel_cls.COMPAT_ENGINES and panel_cls.__name__ not in exclude_panels) or
            ('BLENDER_EEVEE' in panel_cls.COMPAT_ENGINES and panel_cls.__name__ in include_eevee_panels)
        ):
            yield panel_cls

def register():
    register_classes()

    for panel_cls in get_panels():
        panel_cls.COMPAT_ENGINES.add(MoonRayRenderEngine.bl_idname)
    


def unregister():
    unregister_classes()

    for panel_cls in get_panels():
        if MoonRayRenderEngine.bl_idname in panel_cls.COMPAT_ENGINES:
            panel_cls.COMPAT_ENGINES.remove(MoonRayRenderEngine.bl_idname)
    

    