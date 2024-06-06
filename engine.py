import bpy

class MoonRayRenderEngine(bpy.types.HydraRenderEngine):
    bl_idname = "MOONRAY"
    bl_label = "MoonRay"
    bl_info = "Dreamworks' MoonRay Production Renderer integration"

    bl_use_preview = True
    bl_use_gpu_context = True
    bl_use_materialx = True

    bl_delegate_id = "HdStormRendererPlugin"

    def __init__(self):
        self.engine_ptr = None
        pass


    def get_render_settings(self, engine_type):
        settings = bpy.context.scene.moonray.viewport if engine_type == 'VIEWPORT' else \
            bpy.context.scene.moonray.final

        result = {}

        if engine_type != "VIEWPORT":
            result |= {
                'aovToken:Combined': "color",
                'aovToken:Depth': "depth",
            }

        return result
    
    def update_render_passes(self, scene, render_layer):
        if render_layer.use_pass_combined:
            self.register_pass(scene, render_layer, 'Combined', 4, 'RGBA', 'COLOR')
        if render_layer.use_pass_z:
            self.register_pass(scene, render_layer, 'Depth', 1, 'Z', 'VALUE')
    

register, unregister = bpy.utils.register_classes_factory((
    MoonRayRenderEngine,
))