import bpy

from .mfb_panel import MOONRAY_PT_Panel

class MOONRAY_PT_RenderPanel(MOONRAY_PT_Panel):
    bl_label = "MoonRay"
    bl_idname = "MOONRAY_PT_RenderPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"

    def draw(self, context):
        layout = self.layout

class MOONRAY_PT_RenderSettingsPanel(bpy.types.Panel):
    bl_label = "Render Settings"
    bl_idname = "MOONRAY_PT_RenderSettingsPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_parent_id = "MOONRAY_PT_RenderPanel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        moonray = scene.moonray

        layout.prop(moonray, "render_device")
        layout.prop(moonray, "fast_geometry_update")
        layout.prop(moonray, "texture_cache_size")
        layout.prop(moonray, "texture_file_handles")

        # motion_steps

class MOONRAY_PT_RenderSamplesPanel(bpy.types.Panel):
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

        # path_guide_enable
        # bsdf_samples
        # bssrdf_samples

        #disable optimized hair sampling
        # light samples
        # lock_frame_noise

        # max_depth
        # max_diffuse_depth
        # max_glossy_depth
        # max_hair_depth
        # max_mirror_depth
        # max_presence_depth
        # max_subsurface_per_path
        # pixel-samples
        # presence threshold
        # russian_rouleete_threshold
        # transparency threshold

        # max volume depth
        # volume attenuation factor
        # volume contribution_factor
        # volume illumination samples
        # volume_opacity_threshold
        # volume overlap mode
        # volume_phase_attenuation_factor
        # volume_quality
        #volume_shadow_quality

        # light_sampling_mode
        # light_sampling_quality
        
        # max_adaptive_samples
        # min_adaptive_samples

        # sampling_mode


        # batch_tile_order
        # checkpoint_tile_order
        # progressive_tile_order


class MOONRAY_PT_RenderGlobalsPanel(bpy.types.Panel):
    bl_label = "Globals"
    bl_idname = "MOONRAY_PT_RenderGlobalsPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_parent_id = "MOONRAY_PT_RenderPanel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        moonray = scene.moonray

        # enable_displacement
        # enable_dof
        # enable_motion_blur
        # enable_max_geo_resolution
        # enable_presence_shadows
        # enable_shadowing
        # enable_subsurface_scattering
        # lights_visible_in_ca,mera
        # max_geometry_resolution
        # propagate_visiblity_bounce_type
        # shadow_terminator_fix

        # dicing camera



class MOONRAY_PT_RenderDebugPanel(bpy.types.Panel):
    bl_label = "Debug"
    bl_idname = "MOONRAY_PT_RenderDebugPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_parent_id = "MOONRAY_PT_RenderPanel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        moonray = scene.moonray

        # debug console
        # debug pixel
        # validate geometry

        # athena debug
        # fatal_color
        #log_debug
        #log_info
        #stats_file



        layout.prop(moonray, "render_device")
        layout.prop(moonray, "fast_geometry_update")
        layout.prop(moonray, "texture_cache_size")
        layout.prop(moonray, "texture_file_handles")

class MOONRAY_PT_RenderFilteringPanel(bpy.types.Panel):
    bl_label = "Filtering"
    bl_idname = "MOONRAY_PT_RenderFilteringPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_parent_id = "MOONRAY_PT_RenderPanel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        moonray = scene.moonray

        # pixel_filter
        # pixel_filter_width
        # texture_blur

        # roughness clamping
        # sample clamping depth
        # sample clamping value

        

        layout.prop(moonray, "render_device")
        layout.prop(moonray, "fast_geometry_update")
        layout.prop(moonray, "texture_cache_size")
        layout.prop(moonray, "texture_file_handles")

        
classes = [MOONRAY_PT_RenderPanel, MOONRAY_PT_RenderSettingsPanel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)