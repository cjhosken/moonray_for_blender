import bpy

from .mfb_panel import MOONRAY_PT_Panel

class MOONRAY_PT_OutputPanel(MOONRAY_PT_Panel):
    bl_label = "Output"
    bl_idname = "MOONRAY_PT_OutputPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "output"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        moonray = scene.moonray

        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.prop(moonray.output, "channel_format")
        layout.prop(moonray.output, "channel_name")
        layout.prop(moonray.output, "channel_suffix_mode")
        layout.prop(moonray.checkpoint, "checkpoint_active")

        if (moonray.checkpoint.checkpoint_active):
            layout.prop(moonray.output, "checkpoint_file_name")
            layout.prop(moonray.checkpoint, "checkpoint_bg_write")
            layout.prop(moonray.checkpoint, "checkpoint_interval")
            layout.prop(moonray.checkpoint, "checkpoint_max_bgcache")
            layout.prop(moonray.checkpoint, "checkpoint_max_snapshot_overhead")
            layout.prop(moonray.checkpoint, "checkpoint_mode")
            layout.prop(moonray.checkpoint, "checkpoint_overwrite")
            layout.prop(moonray.checkpoint, "checkpoint_post_script")
            layout.prop(moonray.checkpoint, "checkpoint_quality_steps")
            layout.prop(moonray.checkpoint, "checkpoint_checkpoint_sample_cap")
            layout.prop(moonray.checkpoint, "checkpoint_snapshot_interval")
            layout.prop(moonray.checkpoint, "checkpoint_start_sample")
            layout.prop(moonray.checkpoint, "checkpoint_time_cap")
            layout.prop(moonray.checkpoint, "checkpoint_total_files")
            layout.prop(moonray.output, "checkpoint_multi_version_file_name")

        layout.prop(moonray.output, "compression")
        layout.prop(moonray.output, "exr_dwa_compression_level")
        layout.prop(moonray.output, "exr_header_attributes")

        layout.prop(moonray.output, "file_name")
        layout.prop(moonray.output, "file_part")
        layout.prop(moonray.output, "lpe")
        layout.prop(moonray.output, "material_aov")
        layout.prop(moonray.output, "math_filter")
        layout.prop(moonray.output, "output_type")

        layout.prop(moonray.output, "primitive_attribute")
        layout.prop(moonray.output, "primitive_attribute_type")

        layout.prop(moonray.output, "result")
        layout.prop(moonray.output, "resume_file_name")

        layout.prop(moonray.output, "state_variable")
        layout.prop(moonray.output, "visibility_aov")



        
classes = [MOONRAY_PT_OutputPanel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)