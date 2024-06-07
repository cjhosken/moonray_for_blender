import bpy
from ..mfb_nodes import MoonRayCompNode

class MoonRayCompNode_DisplayFilter(MoonRayCompNode):
    bl_idname = 'MoonRayCompNode_DisplayFilter'
    bl_label = 'MoonRay DisplayFilter'

    def init(self, context):
        pass

    def update(self):
        pass


class MoonRayCompNode_BlendDisplayFilter(MoonRayCompNode):
    bl_idname = 'MoonRayCompNode_BlendDisplayFilter'
    bl_label = 'Blend Display'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayCompNode_ClampDisplayFilter(MoonRayCompNode):
    bl_idname = 'MoonRayCompNode_ClampDisplayFilter'
    bl_label = 'Clamp Display'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayCompNode_ColorCorrectDisplayFilter(MoonRayCompNode):
    bl_idname = 'MoonRayCompNode_ColorCorrectDisplayFilter'
    bl_label = 'Color Correct Display'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayCompNode_ConstantDisplayFilter(MoonRayCompNode):
    bl_idname = 'MoonRayCompNode_ConstantDisplayFilter'
    bl_label = 'Constant Display'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayCompNode_ConvolutionDisplayFilter(MoonRayCompNode):
    bl_idname = 'MoonRayCompNode_ConvolutionDisplayFilter'
    bl_label = 'Convolution Display'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayCompNode_DiscretizeDisplayFilter(MoonRayCompNode):
    bl_idname = 'MoonRayCompNode_DiscretizeDisplayFilter'
    bl_label = 'Discretize Display'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayCompNode_DofDisplayFilter(MoonRayCompNode):
    bl_idname = 'MoonRayCompNode_DofDisplayFilter'
    bl_label = 'DOF Display'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayCompNode_HalftoneDisplayFilter(MoonRayCompNode):
    bl_idname = 'MoonRayCompNode_HalftoneDisplayFilter'
    bl_label = 'Halftone Display'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayCompNode_ImageDisplayFilter(MoonRayCompNode):
    bl_idname = 'MoonRayCompNode_ImageDisplayFilter'
    bl_label = 'Image Display'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayCompNode_OpDisplayFilter(MoonRayCompNode):
    bl_idname = 'MoonRayCompNode_OpDisplayFilter'
    bl_label = 'Op Display'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayCompNode_OverDisplayFilter(MoonRayCompNode):
    bl_idname = 'MoonRayCompNode_OverDisplayFilter'
    bl_label = 'Over Display'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayCompNode_RampDisplayFilter(MoonRayCompNode):
    bl_idname = 'MoonRayCompNode_RampDisplayFilter'
    bl_label = 'Ramp Display'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayCompNode_RemapDisplayFilter(MoonRayCompNode):
    bl_idname = 'MoonRayCompNode_RemapDisplayFilter'
    bl_label = 'Remap Display'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayCompNode_RgbToFloatDisplayFilter(MoonRayCompNode):
    bl_idname = 'MoonRayCompNode_RgbToFloatDisplayFilter'
    bl_label = 'RGB to Float Display'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayCompNode_RgbToHsvDisplayFilter(MoonRayCompNode):
    bl_idname = 'MoonRayCompNode_RgbToHsvDisplayFilter'
    bl_label = 'RGB to HSV Display'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayCompNode_ShadowDisplayFilter(MoonRayCompNode):
    bl_idname = 'MoonRayCompNode_ShadowDisplayFilter'
    bl_label = 'Shadow Display'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayCompNode_TangentSpaceDisplayFilter(MoonRayCompNode):
    bl_idname = 'MoonRayCompNode_TangentSpaceDisplayFilter'
    bl_label = 'Tangent Space Display'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayCompNode_ToonDisplayFilter(MoonRayCompNode):
    bl_idname = 'MoonRayCompNode_ToonDisplayFilter'
    bl_label = 'Toon Display'

    def init(self, context):
        pass

    def update(self):
        pass

classes = [
    MoonRayCompNode_BlendDisplayFilter,
    MoonRayCompNode_ClampDisplayFilter,
    MoonRayCompNode_ColorCorrectDisplayFilter,
    MoonRayCompNode_ConstantDisplayFilter,
    MoonRayCompNode_ConvolutionDisplayFilter,
    MoonRayCompNode_DiscretizeDisplayFilter,
    MoonRayCompNode_DofDisplayFilter,
    MoonRayCompNode_HalftoneDisplayFilter,
    MoonRayCompNode_ImageDisplayFilter,
    MoonRayCompNode_OpDisplayFilter,
    MoonRayCompNode_OverDisplayFilter,
    MoonRayCompNode_RampDisplayFilter,
    MoonRayCompNode_RemapDisplayFilter,
    MoonRayCompNode_RgbToFloatDisplayFilter,
    MoonRayCompNode_RgbToHsvDisplayFilter,
    MoonRayCompNode_ShadowDisplayFilter,
    MoonRayCompNode_TangentSpaceDisplayFilter,
    MoonRayCompNode_ToonDisplayFilter,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
