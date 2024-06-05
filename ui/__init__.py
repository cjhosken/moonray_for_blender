import bpy
from bpy.utils import register_class, unregister_class

from .moonray_ui_base import MoonRayPanel
from .moonray_ui_material_panels import classes as ui_material_classes
from .moonray_ui_layer_panels import classes as ui_layer_classes
from .moonray_ui_world_panels import classes as ui_world_classes
from .moonray_ui_render_panels import classes as ui_render_classes
from .moonray_ui_scene_panels import classes as ui_scene_classes
from .moonray_ui_particle_panels import classes as ui_particle_classes
from .moonray_ui_data_panels import classes as ui_data_classes

from bl_ui.properties_render import RENDER_PT_context

classes = ui_material_classes + ui_render_classes + ui_world_classes + ui_layer_classes + ui_scene_classes + ui_particle_classes + ui_data_classes

def get_panels():
    exclude_panels = {
        'VIEWLAYER_PT_filter',
        'VIEWLAYER_PT_layer_passes',
        'RENDER_PT_stereoscopy',
    }

    panels = []
    for panel in bpy.types.Panel.__subclasses__():
        if hasattr(panel, 'COMPAT_ENGINES') and 'BLENDER_RENDER' in panel.COMPAT_ENGINES:
            if panel.__name__ not in exclude_panels:
                panels.append(panel)

    return panels


def moonray_render_draw(panel, context):
    layout = panel.layout

    if not MoonRayPanel.poll(context):
        return

    config = context.scene.moonray.config

    col_device = layout.column(align=True)
    col_device.prop(config, "device", text="Device")
    


def register():
    for cls in classes:
        register_class(cls)

    RENDER_PT_context.append(moonray_render_draw)
    
    for panel in get_panels():
        panel.COMPAT_ENGINES.add('MOONRAY')
    


def unregister():
    for cls in classes:
        unregister_class(cls)

    RENDER_PT_context.remove(moonray_render_draw)

    for panel in get_panels():
        if 'MOONRAY' in panel.COMPAT_ENGINES:
            panel.COMPAT_ENGINES.remove('MOONRAY')
    
    

    