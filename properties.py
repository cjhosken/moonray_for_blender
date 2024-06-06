import bpy


class Properties(bpy.types.PropertyGroup):
    type = None

    @classmethod
    def register(cls):
        cls.type.moonray = bpy.props.PointerProperty(
            name="MoonRay",
            description="MoonRay properties",
            type=cls,
        )

    @classmethod
    def unregister(cls):
        del cls.type.moonray


class MoonRayRenderProperties(bpy.types.PropertyGroup):
    demo: bpy.props.IntProperty()


class MoonRaySceneProperties(Properties):
    type = bpy.types.Scene

    final: bpy.props.PointerProperty(type=MoonRayRenderProperties)
    viewport: bpy.props.PointerProperty(type=MoonRayRenderProperties)


register, unregister = bpy.utils.register_classes_factory((
    MoonRayRenderProperties,
    MoonRaySceneProperties,
))