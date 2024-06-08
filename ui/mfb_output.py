import bpy

from .mfb_panel import MOONRAY_PT_Panel

class MOONRAY_PT_OutputPanel(MOONRAY_PT_Panel):
    bl_label = "Render Samples"
    bl_idname = "MOONRAY_PT_RenderSamplesPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_parent_id = "MOONRAY_PT_RenderPanel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        moonray = scene.moonray

        # exr_header_attributes
        # on_resume_script
        # resumable_output
        # resume_render

        # crypto_uv_attribute_name
        # two_stage_output

        # deep_curvature_tolerance
        # deep_format

        # deep_id_attribute_names
        # deep_vol_compression_res
        # deep_z_tolerance
        #cryptomatte_multi_presence

        #output_file
        #task_distribution_type
        #tmp_dir

        
classes = [MOONRAY_PT_OutputPanel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)