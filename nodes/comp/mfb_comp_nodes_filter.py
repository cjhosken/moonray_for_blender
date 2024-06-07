import bpy
from ..mfb_nodes import MoonRayCompNode

class MoonRayCompNode_Filter(MoonRayCompNode):
    bl_idname = 'MoonRayCompNode_Filter'
    bl_label = 'MoonRay Filter'

    def init(self, context):
        pass

    def update(self):
        pass


classes = [MoonRayCompNode_Filter]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)