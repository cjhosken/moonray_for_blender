import bpy

from . import mfb_node_menus
from ..engine import MoonRayRenderEngine

from . import mfb_light
from . import mfb_object
from . import mfb_view_layer
from . import mfb_render
from . import mfb_output
from . import mfb_menus

def get_panels():
    # Follow the Cycles model of excluding panels we don't want.
    exclude_panels = {
        'DATA_PT_light',
        'DATA_PT_spot',
        'NODE_DATA_PT_light',
        'DATA_PT_falloff_curve',
        'SCENE_PT_audio',


        'RENDER_PT_stamp',
        'RENDER_PT_post_processing',
        'RENDER_PT_simplify',
        'RENDER_PT_freestyle',
        'RENDER_PT_output',
        'RENDER_PT_stereoscopy',
        'RENDER_PT_time_stretching'
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
    mfb_output.register()
    mfb_menus.register()
    mfb_node_menus.register()
    mfb_light.register()
    mfb_object.register()
    mfb_view_layer.register()
    mfb_render.register()

    for panel_cls in get_panels():
        panel_cls.COMPAT_ENGINES.add(MoonRayRenderEngine.bl_idname)

def unregister():
    mfb_output.unregister()
    mfb_menus.unregister()
    mfb_node_menus.unregister()
    mfb_light.unregister()
    mfb_object.unregister()
    mfb_view_layer.unregister()
    mfb_render.unregister()

    for panel_cls in get_panels():
        if MoonRayRenderEngine.bl_idname in panel_cls.COMPAT_ENGINES:
            panel_cls.COMPAT_ENGINES.remove(MoonRayRenderEngine.bl_idname)