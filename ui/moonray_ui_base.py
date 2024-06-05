import bpy

class MoonRayPanel():
    bl_label = "MoonRay Panel"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    COMPAT_ENGINES = ["MOONRAY"]

    @classmethod
    def poll(cls, context):
        return context.engine in cls.COMPAT_ENGINES