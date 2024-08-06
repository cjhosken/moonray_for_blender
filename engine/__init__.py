import bpy

class MoonRayRenderEngine(bpy.types.HydraRenderEngine):
    bl_idname = "MOONRAY"
    bl_label = "MoonRay"
    bl_info = "Dreamworks' MoonRay Production Renderer integration"

    bl_use_preview = True
    bl_use_gpu_context = True
    bl_use_materialx = False

    bl_delegate_id = "HdMoonrayRendererPlugin"

    @classmethod
    def register(cls):
        import pxr.Plug
        pxr.Plug.Registry().RegisterPlugins(['/home/cjhosken/org/dreamworks/installs/plugin'])


    def get_render_settings(self, engine_type):
        settings = bpy.context.scene.moonray

        result = {}

        if engine_type != "VIEWPORT":
            result |= {
                'aovToken:Combined': "color",
                'aovToken:Depth': "depth",
            }

        return result
    
    def update_render_passes(self, scene, render_layer):
        if render_layer.use_pass_z:
            self.register_pass(scene, render_layer, 'Depth', 1, 'Z', 'VALUE')

    def update(self, data, depsgraph):
        super().update(data, depsgraph)


def register():
    bpy.utils.register_class(MoonRayRenderEngine)

def unregister():
    bpy.utils.unregister_class(MoonRayRenderEngine)