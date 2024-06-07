import bpy
from ..mfb_nodes import MoonRayShaderNode

class MoonRayShaderNode_Output(MoonRayShaderNode):
    bl_idname = 'MoonRayShaderNode_Output'
    bl_label = 'MoonRay Output'

    def init(self, context):
        pass

    def update(self):
        pass

classes = [MoonRayShaderNode_Output]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)