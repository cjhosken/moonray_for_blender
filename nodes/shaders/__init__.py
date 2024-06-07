
import  bpy

from .mfb_shader_nodes_output import MoonRayShaderNode_Output
from .mfb_shader_nodes_base import MoonRayShaderNode_Base

classes = [
    MoonRayShaderNode_Output, MoonRayShaderNode_Base
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)