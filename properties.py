import bpy
from bpy.props import PointerProperty, EnumProperty

class MoonRaySceneProperties(bpy.types.PropertyGroup):

    render_device: EnumProperty(
        name="Render Device",
        description="",
        items=[
            ("0", "CPU", "CPU"),
            ("1", "GPU", "GPU"),
        ]
    )

classes = [MoonRaySceneProperties]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.moonray = PointerProperty(type=MoonRaySceneProperties)

def unregister():
    del bpy.types.Scene.moonray

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)