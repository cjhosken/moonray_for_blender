import bpy
from ..mfb_nodes import MoonRayShaderNode

class MoonRayLightShaderNode_BarnDoorLightFilter(MoonRayShaderNode):
    bl_idname = 'MoonRayLightShaderNode_BarnDoorLightFilter'
    bl_label = 'Barn Door'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayLightShaderNode_ColorRampLightFilter(MoonRayShaderNode):
    bl_idname = 'MoonRayLightShaderNode_ColorRampLightFilter'
    bl_label = 'Color Ramp Light Filter'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayLightShaderNode_CombineLightFilter(MoonRayShaderNode):
    bl_idname = 'MoonRayLightShaderNode_CombineLightFilter'
    bl_label = 'Combine Light Filter'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayLightShaderNode_CookieLightFilter(MoonRayShaderNode):
    bl_idname = 'MoonRayLightShaderNode_CookieLightFilter'
    bl_label = 'Cookie Light Filter'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayLightShaderNode_CookieLightFilter_v2(MoonRayShaderNode):
    bl_idname = 'MoonRayLightShaderNode_CookieLightFilter_v2'
    bl_label = 'Cookie Light Filter v2'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayLightShaderNode_DecayLightFilter(MoonRayShaderNode):
    bl_idname = 'MoonRayLightShaderNode_DecayLightFilter'
    bl_label = 'Decay Light Filter'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayLightShaderNode_IntensityLightFilter(MoonRayShaderNode):
    bl_idname = 'MoonRayLightShaderNode_IntensityLightFilter'
    bl_label = 'Intensity Light Filter'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayLightShaderNode_RodLightFilter(MoonRayShaderNode):
    bl_idname = 'MoonRayLightShaderNode_RodLightFilter'
    bl_label = 'Rod Light Filter'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayLightShaderNode_VdbLightFilter(MoonRayShaderNode):
    bl_idname = 'MoonRayLightShaderNode_VdbLightFilter'
    bl_label = 'Vdb Light Filter'

    def init(self, context):
        pass

    def update(self):
        pass

classes = [
    MoonRayLightShaderNode_BarnDoorLightFilter,
    MoonRayLightShaderNode_ColorRampLightFilter,
    MoonRayLightShaderNode_CombineLightFilter,
    MoonRayLightShaderNode_CookieLightFilter,
    MoonRayLightShaderNode_CookieLightFilter_v2,
    MoonRayLightShaderNode_DecayLightFilter,
    MoonRayLightShaderNode_IntensityLightFilter,
    MoonRayLightShaderNode_RodLightFilter,
    MoonRayLightShaderNode_VdbLightFilter
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
