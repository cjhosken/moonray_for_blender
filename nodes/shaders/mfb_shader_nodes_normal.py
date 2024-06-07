import bpy
from ..mfb_nodes import MoonRayShaderNode

class MoonRayShaderNode_CombineNormalMap(MoonRayShaderNode):
    bl_idname = 'MoonRayShaderNode_CombineNormalMap'
    bl_label = 'Combine Normal Map'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayShaderNode_DistortNormalMap(MoonRayShaderNode):
    bl_idname = 'MoonRayShaderNode_DistortNormalMap'
    bl_label = 'Distort Normal Map'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayShaderNode_ImageNormalMap(MoonRayShaderNode):
    bl_idname = 'MoonRayShaderNode_ImageNormalMap'
    bl_label = 'Image Normal Map'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayShaderNode_ProjectCameraNormalMap(MoonRayShaderNode):
    bl_idname = 'MoonRayShaderNode_ProjectCameraNormalMap'
    bl_label = 'Project Camera Normal Map'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayShaderNode_ProjectPlanarNormalMap(MoonRayShaderNode):
    bl_idname = 'MoonRayShaderNode_ProjectPlanarNormalMap'
    bl_label = 'Project Planar Normal Map'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayShaderNode_ProjectTriPlanarNormalMap(MoonRayShaderNode):
    bl_idname = 'MoonRayShaderNode_ProjectTriPlanarNormalMap'
    bl_label = 'Project TriPlanar Normal Map'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayShaderNode_RandomNormalMap(MoonRayShaderNode):
    bl_idname = 'MoonRayShaderNode_RandomNormalMap'
    bl_label = 'Random Normal Map'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayShaderNode_RgbToNormalMap(MoonRayShaderNode):
    bl_idname = 'MoonRayShaderNode_RgbToNormalMap'
    bl_label = 'RGB to Normal Map'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayShaderNode_SwitchNormalMap(MoonRayShaderNode):
    bl_idname = 'MoonRayShaderNode_SwitchNormalMap'
    bl_label = 'Switch Normal Map'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayShaderNode_TransformNormalMap(MoonRayShaderNode):
    bl_idname = 'MoonRayShaderNode_TransformNormalMap'
    bl_label = 'Transform Normal Map'

    def init(self, context):
        pass

    def update(self):
        pass

classes = [
    MoonRayShaderNode_CombineNormalMap,
    MoonRayShaderNode_DistortNormalMap,
    MoonRayShaderNode_ImageNormalMap,
    MoonRayShaderNode_ProjectCameraNormalMap,
    MoonRayShaderNode_ProjectPlanarNormalMap,
    MoonRayShaderNode_ProjectTriPlanarNormalMap,
    MoonRayShaderNode_RandomNormalMap,
    MoonRayShaderNode_RgbToNormalMap,
    MoonRayShaderNode_SwitchNormalMap,
    MoonRayShaderNode_TransformNormalMap
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

