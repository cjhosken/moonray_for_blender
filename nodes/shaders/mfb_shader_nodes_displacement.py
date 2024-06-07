import bpy
from ..mfb_nodes import MoonRayShaderNode

class MoonRayShaderNode_CombineDisplacement(MoonRayShaderNode):
    bl_idname = 'MoonRayShaderNode_CombineDisplacement'
    bl_label = 'Combine Displacement'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayShaderNode_NormalDisplacement(MoonRayShaderNode):
    bl_idname = 'MoonRayShaderNode_NormalDisplacement'
    bl_label = 'Normal Displacement'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayShaderNode_SwitchDisplacement(MoonRayShaderNode):
    bl_idname = 'MoonRayShaderNode_SwitchDisplacement'
    bl_label = 'Switch Displacement'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayShaderNode_VectorDisplacement(MoonRayShaderNode):
    bl_idname = 'MoonRayShaderNode_VectorDisplacement'
    bl_label = 'Vector Displacement'

    def init(self, context):
        pass

    def update(self):
        pass


classes = [
    MoonRayShaderNode_CombineDisplacement,
    MoonRayShaderNode_NormalDisplacement,
    MoonRayShaderNode_SwitchDisplacement,
    MoonRayShaderNode_VectorDisplacement
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)