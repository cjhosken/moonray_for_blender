import bpy

from .mfb_panel import MOONRAY_PT_Panel
from ..engine import MoonRayRenderEngine

class MOONRAY_PT_RenderPanel(MOONRAY_PT_Panel):
    bl_label = "MoonRay"
    bl_idname = "MOONRAY_PT_RenderPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"

    def draw(self, context):
        layout = self.layout

class MOONRAY_PT_RenderSettingsPanel(MOONRAY_PT_Panel):
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

        layout.prop(moonray.path_guide, "path_guide_enable")

class MOONRAY_PT_RenderGlobalsPanel(MOONRAY_PT_Panel):
    bl_label = "Render Globals"
    bl_idname = "MOONRAY_PT_RenderGlobalsPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_parent_id = "MOONRAY_PT_RenderSettingsPanel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        moonray = scene.moonray

        layout.prop(moonray.global_toggles, "enable_displacement")
        layout.prop(moonray.global_toggles, "enable_dof")
        layout.prop(moonray.global_toggles, "enable_max_geometry_resolution")
        layout.prop(moonray.global_toggles, "enable_motion_blur")
        layout.prop(moonray.global_toggles, "enable_presence_shadows")
        layout.prop(moonray.global_toggles, "enable_shadowing")
        layout.prop(moonray.global_toggles, "enable_subsurface_scattering")
        layout.prop(moonray.global_toggles, "lights_visible_in_camera")
        layout.prop(moonray.global_toggles, "max_geometry_resolution")
        layout.prop(moonray.global_toggles, "propagate_visibility_bounce_type")
        layout.prop(moonray.global_toggles, "shadow_terminator_fix")


class MOONRAY_PT_RenderSamplesPanel(MOONRAY_PT_Panel):
    bl_label = "Render Samples"
    bl_idname = "MOONRAY_PT_RenderSamplesPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_parent_id = "MOONRAY_PT_RenderSettingsPanel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        moonray = scene.moonray

        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.prop(moonray.sampling, "bsdf_samples")
        layout.prop(moonray.sampling, "bssrdf_samples")
        layout.prop(moonray.sampling, "disable_optimized_hair_sampling")
        layout.prop(moonray.sampling, "light_samples")
        layout.prop(moonray.sampling, "lock_frame_noise")
        layout.prop(moonray.sampling, "max_depth")
        layout.prop(moonray.sampling, "max_diffuse_depth")
        layout.prop(moonray.sampling, "max_glossy_depth")
        layout.prop(moonray.sampling, "max_hair_depth")
        layout.prop(moonray.sampling, "max_presence_depth")
        layout.prop(moonray.sampling, "max_subsurface_per_path")
        layout.prop(moonray.sampling, "pixel_samples")
        layout.prop(moonray.sampling, "presence_threshold")
        layout.prop(moonray.sampling, "russian_roulette_threshold")
        layout.prop(moonray.sampling, "transparency_threshold")

class MOONRAY_PT_RenderVolumePanel(MOONRAY_PT_Panel):
    bl_label = "Volume"
    bl_idname = "MOONRAY_PT_RenderVolumePanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_parent_id = "MOONRAY_PT_RenderSamplesPanel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        moonray = scene.moonray

        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.prop(moonray.volumes, "max_volume_depth")
        layout.prop(moonray.volumes, "volume_attenuation_factor")
        layout.prop(moonray.volumes, "volume_contribution_factor")
        layout.prop(moonray.volumes, "volume_illumination_samples")
        layout.prop(moonray.volumes, "volume_opacity_threshold")
        layout.prop(moonray.volumes, "volume_overlap_mode")
        layout.prop(moonray.volumes, "volume_phase_attenuation_factor")
        layout.prop(moonray.volumes, "volume_quality")
        layout.prop(moonray.volumes, "volume_shadow_quality")

class MOONRAY_PT_RenderFilteringPanel(MOONRAY_PT_Panel):
    bl_label = "Filtering"
    bl_idname = "MOONRAY_PT_RenderFilteringPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_parent_id = "MOONRAY_PT_RenderSamplesPanel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        moonray = scene.moonray

        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.prop(moonray.fireflies_removal, "roughness_clamping_factor")
        layout.prop(moonray.fireflies_removal, "sample_clamping_depth")
        layout.prop(moonray.fireflies_removal, "sample_clamping_value")

        layout.prop(moonray.filtering, "pixel_filter")
        layout.prop(moonray.filtering, "pixel_filter_width")
        layout.prop(moonray.filtering, "texture_blur")

        
classes = [MOONRAY_PT_RenderPanel, MOONRAY_PT_RenderSettingsPanel, MOONRAY_PT_RenderGlobalsPanel, MOONRAY_PT_RenderSamplesPanel, MOONRAY_PT_RenderVolumePanel, MOONRAY_PT_RenderFilteringPanel]




def render_header_draw(self, context):
    if context.scene.render.engine == MoonRayRenderEngine.bl_idname:
        layout = self.layout
        scene = context.scene
        moonray = scene.moonray
        
        self.layout.prop(moonray.mfb, "execution_mode")

def register():
    bpy.types.RENDER_PT_context.append(render_header_draw)

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    bpy.types.RENDER_PT_context.remove(render_header_draw)

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)