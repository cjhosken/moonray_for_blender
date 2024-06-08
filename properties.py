import bpy
from bpy.props import *

from .mfb.sets import MoonRayLightSets, MoonRayLightFilterSets, MoonRayShadowSets, MoonRayShadowReceiverSets, MoonRayTraceSets

class MoonRaySceneProperties(bpy.types.PropertyGroup):

    render_device: EnumProperty(
        name="Render Device",
        description="",
        items=[
            ("0", "CPU", "CPU"),
            ("1", "GPU", "GPU"),
        ]
    )

    fast_geometry_update : BoolProperty(name="Fast Geo Updaate")
    
    texture_cache_size : IntProperty(name="Texture Cache Size")
    texture_file_handles : IntProperty(name="Texture fIle Handles")

    light_sets: PointerProperty(type=MoonRayLightSets)
    lightfilter_sets: PointerProperty(type=MoonRayLightFilterSets)
    shadow_sets: PointerProperty(type=MoonRayShadowSets)
    shadowreceiver_sets: PointerProperty(type=MoonRayShadowReceiverSets)
    trace_sets: PointerProperty(type=MoonRayTraceSets)

class MoonRayLightProperties(bpy.types.PropertyGroup):
    visible : BoolProperty(name="Visible")
    motion_blur : BoolProperty(name="Motion Blur")
    texture : StringProperty(name="Texture", subtype="FILE_PATH")

    type : EnumProperty(
        name="Light Type",
        description="Choose a light type",
        items=[
            ('CYLINDER', 'Cylinder', ''),
            ('DISK', 'Disk', ''),
            ('DISTANT', 'Distant', ''),
            ('ENV', 'Environment', ''),
            ('RECT', 'Rect', ''),
            ('SPHERE', 'Sphere', ''),
            ('SPOT', 'Spot', '')
        ]
    )

    lightfilter_set: StringProperty(name="Light Filter Set")
    light_set_input: StringProperty(name="Light Sets")
    shadow_set_input: StringProperty(name="Shadow Sets")

class MoonRayObjectProperties(bpy.types.PropertyGroup):
    is_light : BoolProperty(name="Is Light Source")

    light_set: StringProperty(name="Light Set")
    shadow_set: StringProperty(name="Shadow Set")
    shadow_receiver_set: StringProperty(name="Shadow Receiver Set")
    trace_set_input: StringProperty(name="Trace Set")
    shadowreceiver_set_input: StringProperty(name="Shadow Receiver Set")


classes = [MoonRaySceneProperties, MoonRayLightProperties, MoonRayObjectProperties]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.moonray = PointerProperty(type=MoonRaySceneProperties)
    bpy.types.Light.moonray = PointerProperty(type=MoonRayLightProperties)
    bpy.types.Object.moonray = PointerProperty(type=MoonRayObjectProperties)


def unregister():
    del bpy.types.Scene.moonray
    del bpy.types.Object.moonray
    del bpy.types.Light.moonray

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)