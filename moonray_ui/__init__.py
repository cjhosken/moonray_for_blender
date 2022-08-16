from bpy.utils import register_class, unregister_class
from bpy.types import Panel
from .moonray_ui_base import classes as ui_base_classes
from .moonray_ui_material_panels import classes as ui_material_classes
from .moonray_ui_layer_panels import classes as ui_layer_classes
from .moonray_ui_world_panels import classes as ui_world_classes
from .moonray_ui_render_panels import classes as ui_render_classes

classes = ui_base_classes + ui_material_classes + ui_render_classes + ui_world_classes + ui_layer_classes


def get_panels():
    exclude_panels = {
        'VIEWLAYER_PT_filter',
        'VIEWLAYER_PT_layer_passes',
        'RENDER_PT_stereoscopy'
    }

    panels = []
    for panel in Panel.__subclasses__():
        if hasattr(panel, 'COMPAT_ENGINES') and 'BLENDER_RENDER' in panel.COMPAT_ENGINES:
            if panel.__name__ not in exclude_panels:
                panels.append(panel)

    return panels

def register():
    for cls in classes:
        register_class(cls)
    
    for panel in get_panels():
        panel.COMPAT_ENGINES.add('MOONRAY')

def unregister():
    for cls in classes:
        unregister_class(cls)

    for panel in get_panels():
        if 'MOONRAY' in panel.COMPAT_ENGINES:
            panel.COMPAT_ENGINES.remove('MOONRAY')
    

    