import bpy
from bpy.types import AddonPreferences
from bpy.props import StringProperty


class MoonRayPreferences(AddonPreferences):
    bl_idname = __name__

    moonray_path: StringProperty(
        name="MoonRay Path",
        description="Path to the MoonRay executable",
        subtype='FILE_PATH',
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="MoonRay Settings")
        layout.prop(self, "moonray_path")

def register():
    bpy.utils.register_class(MoonRayPreferences)

def unregister():
    bpy.utils.unregister_class(MoonRayPreferences)