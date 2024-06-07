import bpy
from ..mfb_nodes import MoonRayShaderNode

class MoonRayShaderNode_Base(MoonRayShaderNode):
    bl_idname = 'MoonRayShaderNode_Base'
    bl_label = 'MoonRay Node'

    def init(self, context):
        pass

    def update(self):
        pass