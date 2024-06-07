import bpy

class MoonRayShaderNode(bpy.types.ShaderNode):
    bl_idname = 'MoonRayShaderNode'
    bl_label = 'MoonRay Shader Node'

    def init(self, context):
        pass

    def update(self):
        pass

class MoonRayCompNode(bpy.types.CompositorNode):
    bl_idname = 'MoonRayCompNode'
    bl_label = 'MoonRay Comp Node'

    def init(self, context):
        pass

    def update(self):
        pass