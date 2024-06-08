import bpy
from ..mfb_nodes import MoonRayShaderNode

class MoonRayShaderNode_Output(MoonRayShaderNode):
    bl_idname = 'MoonRayShaderNode_Output'
    bl_label = 'MoonRay Output'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayShaderNode_BakeCamera(MoonRayShaderNode):
    bl_idname = 'MoonRayShaderNode_BakeCamera'
    bl_label = 'MoonRay Bake Camera'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayLightShaderNode_Output(MoonRayShaderNode):
    bl_idname = 'MoonRayLightShaderNode_Output'
    bl_label = 'MoonRay Light Output'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayWorldShaderNode_Output(MoonRayShaderNode):
    bl_idname = 'MoonRayWorldShaderNode_Output'
    bl_label = 'MoonRay World Output'

    def init(self, context):
        pass

    def update(self):
        pass

classes = [MoonRayShaderNode_Output, MoonRayShaderNode_BakeCamera, MoonRayLightShaderNode_Output, MoonRayWorldShaderNode_Output]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)