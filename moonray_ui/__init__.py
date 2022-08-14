from bpy.utils import register_class, unregister_class
from .moonray_ui_base import classes as ui_base_classes
from .moonray_ui_material_panels import classes as ui_material_classes
from .moonray_ui_render_panels import classes as ui_render_classes

classes = ui_base_classes + ui_material_classes + ui_render_classes

def register():
    for cls in classes:
        register_class(cls)

def unregister():
    for cls in classes:
        unregister_class(cls)
    

    