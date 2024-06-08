import bpy
from bpy.props import *


class MoonRayPreferences(bpy.types.AddonPreferences):
    bl_idname = "moonray_for_blender"

    moonray_path: StringProperty(
        name="MoonRay Path",
        description="Path to the MoonRay executable",
        subtype='FILE_PATH'
    )

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        moonray = scene.moonray
    

        layout.label(text="Global")
        layout.prop(self, "moonray_path")
        layout.prop(moonray.driver, "output_file")
        layout.prop(moonray.driver, "tmp_dir")

        layout.label(text="Debugging")
        layout.prop(moonray.debug, "debug_console")
        layout.prop(moonray.debug, "debug_pixel")
        layout.prop(moonray.debug, "validate_geometry")

        layout.label(text="Driver")
        layout.prop(moonray.driver, "machine_id")
        layout.prop(moonray.driver, "num_machines")
        layout.prop(moonray.driver, "task_distribution_type")

        layout.label(text="Caching")
        layout.prop(moonray.caching, "fast_geometry_update")
        layout.prop(moonray.caching, "texture_cache_size")
        layout.prop(moonray.caching, "texture_file_handles")

        layout.label(text="Logging")
        layout.prop(moonray.logging, "athena_debug")
        layout.prop(moonray.logging, "fatal_color")
        layout.prop(moonray.logging, "log_debug")
        layout.prop(moonray.logging, "log_info")

def register():
    bpy.utils.register_class(MoonRayPreferences)

def unregister():
    bpy.utils.unregister_class(MoonRayPreferences)