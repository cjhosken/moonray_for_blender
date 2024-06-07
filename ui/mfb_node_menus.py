import bpy

from ..engine import MoonRayRenderEngine

class MoonRayShaderNodeMenu(bpy.types.Menu):
    bl_idname = "NODE_MT_shader_node_add_moonray"
    bl_label = "Add MoonRay Node"

    def draw(self, context):
        layout = self.layout
        layout.menu("NODE_MT_shader_node_add_moonray_shader", text="Shader")
        layout.menu("NODE_MT_shader_node_add_moonray_map", text="Map")
        layout.menu("NODE_MT_shader_node_add_moonray_output", text="Output")
        layout.menu("NODE_MT_shader_node_add_moonray_normal", text="Normal")
        layout.menu("NODE_MT_shader_node_add_moonray_disp", text="Displacement")

class MoonRayShaderNodeMenu_Shader(bpy.types.Menu):
    bl_idname = "NODE_MT_shader_node_add_moonray_shader"
    bl_label = "Add MoonRay Node"

    def draw(self, context):
        layout = self.layout
        layout.operator("node.add_moonray_node", text="Axf").type = 'MoonRayShaderNode_Axf'
        layout.operator("node.add_moonray_node", text="Measured").type = 'MoonRayShaderNode_Measured'
        layout.operator("node.add_moonray_node", text="Ray Switch").type = 'MoonRayShaderNode_RaySwitch'
        layout.operator("node.add_moonray_node", text="Switch").type = 'MoonRayShaderNode_Switch'
        layout.operator("node.add_moonray_node", text="UsdPreviewSurface").type = 'MoonRayShaderNode_UsdPreviewSurface'
        layout.operator("node.add_moonray_node", text="DwaColorCorrect").type = 'MoonRayShaderNode_DwaColorCorrect'
        layout.operator("node.add_moonray_node", text="DwaLayer").type = 'MoonRayShaderNode_DwaLayer'
        layout.operator("node.add_moonray_node", text="DwaRefractive").type = 'MoonRayShaderNode_DwaRefractive'
        layout.operator("node.add_moonray_node", text="DwaSwitch").type = 'MoonRayShaderNode_DwaSwitch'
        layout.operator("node.add_moonray_node", text="GlitterFlake").type = 'MoonRayShaderNode_GlitterFlake'
        layout.operator("node.add_moonray_node", text="HairDiffuse").type = 'MoonRayShaderNode_HairDiffuse'
        layout.operator("node.add_moonray_node", text="Toon").type = 'MoonRayShaderNode_Toon'
        layout.operator("node.add_moonray_node", text="HairToon").type = 'MoonRayShaderNode_HairToon'
        layout.operator("node.add_moonray_node", text="DwaAdjust").type = 'MoonRayShaderNode_DwaAdjust'
        layout.operator("node.add_moonray_node", text="DwaEmissive").type = 'MoonRayShaderNode_DwaEmissive'
        layout.operator("node.add_moonray_node", text="DwaMetal").type = 'MoonRayShaderNode_DwaMetal'
        layout.operator("node.add_moonray_node", text="DwaSkin").type = 'MoonRayShaderNode_DwaSkin'
        layout.operator("node.add_moonray_node", text="DwaTwoSided").type = 'MoonRayShaderNode_DwaTwoSided'
        layout.operator("node.add_moonray_node", text="Hair").type = 'MoonRayShaderNode_Hair'
        layout.operator("node.add_moonray_node", text="HairLayer").type = 'MoonRayShaderNode_HairLayer'
        layout.operator("node.add_moonray_node", text="DwaBase").type = 'MoonRayShaderNode_DwaBase'
        layout.operator("node.add_moonray_node", text="DwaFabric").type = 'MoonRayShaderNode_DwaFabric'
        layout.operator("node.add_moonray_node", text="DwaMix").type = 'MoonRayShaderNode_DwaMix'
        layout.operator("node.add_moonray_node", text="DwaSolidDielectric").type = 'MoonRayShaderNode_DwaSolidDielectric'
        layout.operator("node.add_moonray_node", text="DwaVelvet").type = 'MoonRayShaderNode_DwaVelvet'
        layout.operator("node.add_moonray_node", text="HairColorCorrect").type = 'MoonRayShaderNode_HairColorCorrect'
        layout.operator("node.add_moonray_node", text="MacroFlake").type = 'MoonRayShaderNode_MacroFlake'

class MoonRayShaderNodeMenu_Map(bpy.types.Menu):
    bl_idname = "NODE_MT_shader_node_add_moonray_map"
    bl_label = "Add MoonRay Node"

    def draw(self, context):
        layout = self.layout
        layout.operator("node.add_moonray_node", text="Attribute").type = 'MoonRayShaderNode_Map_Attribute'
        layout.operator("node.add_moonray_node", text="Debug").type = 'MoonRayShaderNode_Map_Debug'
        layout.operator("node.add_moonray_node", text="List").type = 'MoonRayShaderNode_Map_List'
        layout.operator("node.add_moonray_node", text="UsdPrimvarReader_float2").type = 'MoonRayShaderNode_Map_UsdPrimvarReader_float2'
        layout.operator("node.add_moonray_node", text="UsdPrimvarReader_point").type = 'MoonRayShaderNode_Map_UsdPrimvarReader_point'
        layout.operator("node.add_moonray_node", text="UsdUVTexture").type = 'MoonRayShaderNode_Map_UsdUVTexture'
        layout.operator("node.add_moonray_node", text="Checkerboard").type = 'MoonRayShaderNode_Map_Checkerboard'
        layout.operator("node.add_moonray_node", text="ExtraAov").type = 'MoonRayShaderNode_Map_ExtraAov'
        layout.operator("node.add_moonray_node", text="OpenVdb").type = 'MoonRayShaderNode_Map_OpenVdb'
        layout.operator("node.add_moonray_node", text="UsdPrimvarReader_float3").type = 'MoonRayShaderNode_Map_UsdPrimvarReader_float3'
        layout.operator("node.add_moonray_node", text="UsdPrimvarReader_vector").type = 'MoonRayShaderNode_Map_UsdPrimvarReader_vector'
        layout.operator("node.add_moonray_node", text="Image").type = 'MoonRayShaderNode_Map_Image'
        layout.operator("node.add_moonray_node", text="UsdPrimvarReader_float").type = 'MoonRayShaderNode_Map_UsdPrimvarReader_float'
        layout.operator("node.add_moonray_node", text="UsdPrimvarReader_int").type = 'MoonRayShaderNode_Map_UsdPrimvarReader_int'
        layout.operator("node.add_moonray_node", text="UsdTransform2d").type = 'MoonRayShaderNode_Map_UsdTransform2d'
        layout.operator("node.add_moonray_node", text="AxisAngle").type = 'MoonRayShaderNode_Map_AxisAngle'
        layout.operator("node.add_moonray_node", text="ColorCorrectLegacy").type = 'MoonRayShaderNode_Map_ColorCorrectLegacy'
        layout.operator("node.add_moonray_node", text="Directional").type = 'MoonRayShaderNode_Map_Directional'
        layout.operator("node.add_moonray_node", text="LOD").type = 'MoonRayShaderNode_Map_LOD'
        layout.operator("node.add_moonray_node", text="ProjectSpherical").type = 'MoonRayShaderNode_Map_ProjectSpherical'
        layout.operator("node.add_moonray_node", text="SwitchColor").type = 'MoonRayShaderNode_Map_SwitchColor'
        layout.operator("node.add_moonray_node", text="Blend").type = 'MoonRayShaderNode_Map_Blend'
        layout.operator("node.add_moonray_node", text="ColorCorrect").type = 'MoonRayShaderNode_Map_ColorCorrect'
        layout.operator("node.add_moonray_node", text="FloatToRgb").type = 'MoonRayShaderNode_Map_FloatToRgb'
        layout.operator("node.add_moonray_node", text="Noise").type = 'MoonRayShaderNode_Map_Noise'
        layout.operator("node.add_moonray_node", text="ProjectTriplanar").type = 'MoonRayShaderNode_Map_ProjectTriplanar'
        layout.operator("node.add_moonray_node", text="SwitchFloat").type = 'MoonRayShaderNode_Map_SwitchFloat'
        layout.operator("node.add_moonray_node", text="Clamp").type = 'MoonRayShaderNode_Map_Clamp'
        layout.operator("node.add_moonray_node", text="ColorCorrectNuke").type = 'MoonRayShaderNode_Map_ColorCorrectNuke'
        layout.operator("node.add_moonray_node", text="Gradient").type = 'MoonRayShaderNode_Map_Gradient'
        layout.operator("node.add_moonray_node", text="NoiseWorley").type = 'MoonRayShaderNode_Map_NoiseWorley'
        layout.operator("node.add_moonray_node", text="ProjectTriplanarUdim").type = 'MoonRayShaderNode_Map_ProjectTriplanarUdim'
        layout.operator("node.add_moonray_node", text="Template").type = 'MoonRayShaderNode_Map_Template'
        layout.operator("node.add_moonray_node", text="ColorCorrectSaturation").type = 'MoonRayShaderNode_Map_ColorCorrectSaturation'
        layout.operator("node.add_moonray_node", text="HairColorPresets").type = 'MoonRayShaderNode_Map_HairColorPresets'
        layout.operator("node.add_moonray_node", text="NormalToRgb").type = 'MoonRayShaderNode_Map_NormalToRgb'
        layout.operator("node.add_moonray_node", text="Ramp").type = 'MoonRayShaderNode_Map_Ramp'
        layout.operator("node.add_moonray_node", text="Toon").type = 'MoonRayShaderNode_Map_Toon'
        layout.operator("node.add_moonray_node", text="ColorCorrectContrast").type = 'MoonRayShaderNode_Map_ColorCorrectContrast'
        layout.operator("node.add_moonray_node", text="ColorCorrectTMI").type = 'MoonRayShaderNode_Map_ColorCorrectTMI'
        layout.operator("node.add_moonray_node", text="HairColumn").type = 'MoonRayShaderNode_Map_HairColumn'
        layout.operator("node.add_moonray_node", text="Op").type = 'MoonRayShaderNode_Map_Op'
        layout.operator("node.add_moonray_node", text="Random").type = 'MoonRayShaderNode_Map_Random'
        layout.operator("node.add_moonray_node", text="TransformNormal").type = 'MoonRayShaderNode_Map_TransformNormal'
        layout.operator("node.add_moonray_node", text="ColorCorrectGainOffset").type = 'MoonRayShaderNode_Map_ColorCorrectGainOffset'
        layout.operator("node.add_moonray_node", text="ConstantColor").type = 'MoonRayShaderNode_Map_ConstantColor'
        layout.operator("node.add_moonray_node", text="Hair").type = 'MoonRayShaderNode_Map_Hair'
        layout.operator("node.add_moonray_node", text="OpSqrt").type = 'MoonRayShaderNode_Map_OpSqrt'
        layout.operator("node.add_moonray_node", text="Remap").type = 'MoonRayShaderNode_Map_Remap'
        layout.operator("node.add_moonray_node", text="TransformSpace").type = 'MoonRayShaderNode_Map_TransformSpace'
        layout.operator("node.add_moonray_node", text="ColorCorrectGamma").type = 'MoonRayShaderNode_Map_ColorCorrectGamma'
        layout.operator("node.add_moonray_node", text="ConstantScalar").type = 'MoonRayShaderNode_Map_ConstantScalar'
        layout.operator("node.add_moonray_node", text="HsvToRgb").type = 'MoonRayShaderNode_Map_HsvToRgb'
        layout.operator("node.add_moonray_node", text="ProjectCamera").type = 'MoonRayShaderNode_Map_ProjectCamera'
        layout.operator("node.add_moonray_node", text="RgbToFloat").type = 'MoonRayShaderNode_Map_RgbToFloat'
        layout.operator("node.add_moonray_node", text="UVTransform").type = 'MoonRayShaderNode_Map_UVTransform'
        layout.operator("node.add_moonray_node", text="ColorCorrectHsv").type = 'MoonRayShaderNode_Map_ColorCorrectHsv'
        layout.operator("node.add_moonray_node", text="Curvature").type = 'MoonRayShaderNode_Map_Curvature'
        layout.operator("node.add_moonray_node", text="Layer").type = 'MoonRayShaderNode_Map_Layer'
        layout.operator("node.add_moonray_node", text="ProjectCylindrical").type = 'MoonRayShaderNode_Map_ProjectCylindrical'
        layout.operator("node.add_moonray_node", text="RgbToHsv").type = 'MoonRayShaderNode_Map_RgbToHsv'
        layout.operator("node.add_moonray_node", text="Wireframe").type = 'MoonRayShaderNode_Map_Wireframe'
        layout.operator("node.add_moonray_node", text="ColorCorrectHueShift").type = 'MoonRayShaderNode_Map_ColorCorrectHueShift'
        layout.operator("node.add_moonray_node", text="Deformation").type = 'MoonRayShaderNode_Map_Deformation'
        layout.operator("node.add_moonray_node", text="LcToRgb").type = 'MoonRayShaderNode_Map_LcToRgb'
        layout.operator("node.add_moonray_node", text="ProjectPlanar").type = 'MoonRayShaderNode_Map_ProjectPlanar'
        layout.operator("node.add_moonray_node", text="RgbToLab").type = 'MoonRayShaderNode_Map_RgbToLab'

class MoonRayShaderNodeMenu_Displacement(bpy.types.Menu):
    bl_idname = "NODE_MT_shader_node_add_moonray_disp"
    bl_label = "Add MoonRay Node"

    def draw(self, context):
        layout = self.layout
        layout.operator("node.add_moonray_node", text="Combine Displacement").type = 'MoonRayShaderNode_CombineDisplacement'
        layout.operator("node.add_moonray_node", text="Normal Displacement").type = 'MoonRayShaderNode_NormalDisplacement'
        layout.operator("node.add_moonray_node", text="Switch Displacement").type = 'MoonRayShaderNode_SwitchDisplacement'
        layout.operator("node.add_moonray_node", text="Vector Displacement").type = 'MoonRayShaderNode_VectorDisplacement'

class MoonRayShaderNodeMenu_Normal(bpy.types.Menu):
    bl_idname = "NODE_MT_shader_node_add_moonray_normal"
    bl_label = "Add MoonRay Node"

    def draw(self, context):
        layout = self.layout
        layout.operator("node.add_moonray_node", text="Combine Normal Map").type = 'MoonRayShaderNode_CombineNormalMap'
        layout.operator("node.add_moonray_node", text="Distort Normal Map").type = 'MoonRayShaderNode_DistortNormalMap'
        layout.operator("node.add_moonray_node", text="Image Normal Map").type = 'MoonRayShaderNode_ImageNormalMap'
        layout.operator("node.add_moonray_node", text="Project Camera Normal Map").type = 'MoonRayShaderNode_ProjectCameraNormalMap'
        layout.operator("node.add_moonray_node", text="Project Planar Normal Map").type = 'MoonRayShaderNode_ProjectPlanarNormalMap'
        layout.operator("node.add_moonray_node", text="Project Triplanar Normal Map").type = 'MoonRayShaderNode_ProjectTriplanarNormalMap'
        layout.operator("node.add_moonray_node", text="Project Triplanar Normal Map (v2)").type = 'MoonRayShaderNode_ProjectTriplanarNormalMap_v2'
        layout.operator("node.add_moonray_node", text="Random Normal Map").type = 'MoonRayShaderNode_RandomNormalMap'
        layout.operator("node.add_moonray_node", text="Rgb to Normal Map").type = 'MoonRayShaderNode_RgbToNormalMap'
        layout.operator("node.add_moonray_node", text="Switch Normal Map").type = 'MoonRayShaderNode_SwitchNormalMap'
        layout.operator("node.add_moonray_node", text="Transform Normal Map").type = 'MoonRayShaderNode_TransformNormalMap'


class MoonRayShaderNodeMenu_Output(bpy.types.Menu):
    bl_idname = "NODE_MT_shader_node_add_moonray_output"
    bl_label = "Add MoonRay Node"

    def draw(self, context):
        layout = self.layout
        layout.operator("node.add_moonray_node", text="MoonRay Output").type = 'MoonRayShaderNode_Output'
        layout.operator("node.add_moonray_node", text="Bake Camera").type = 'MoonRayShaderNode_BakeCamera'



# Light Nodes
class MoonRayLightShaderNodeMenu(bpy.types.Menu):
    bl_idname = "NODE_MT_lightshader_node_add_moonray"
    bl_label = "Add MoonRay Node"

    def draw(self, context):
        layout = self.layout
        layout.menu("NODE_MT_lightshader_node_add_moonray_lightfilter", text="Light Filter")
        layout.menu("NODE_MT_lightshader_node_add_moonray_output", text="Output")

class MoonRayLightShaderNodeMenu_LightFilter(bpy.types.Menu):
    bl_idname = "NODE_MT_lightshader_node_add_moonray_lightfilter"
    bl_label = "Add MoonRay Node"

    def draw(self, context):
        layout = self.layout
        layout.operator("node.add_moonray_node", text="Barndoor Light Filter").type = 'MoonRayLightShaderNode_BarnDoorLightFilter'
        layout.operator("node.add_moonray_node", text="Color Ramp Light Filter").type = 'MoonRayLightShaderNode_ColorRampLightFilter'
        layout.operator("node.add_moonray_node", text="Combine Light Filter").type = 'MoonRayLightShaderNode_CombineLightFilter'
        layout.operator("node.add_moonray_node", text="Cookie Light Filter").type = 'MoonRayLightShaderNode_CookieLightFilter'
        layout.operator("node.add_moonray_node", text="Cookie Light Filter (v2)").type = 'MoonRayLightShaderNode_CookieLightFilter_v2'
        layout.operator("node.add_moonray_node", text="Decay Light Filter").type = 'MoonRayLightShaderNode_DecayLightFilter'
        layout.operator("node.add_moonray_node", text="Intensity Light Filter").type = 'MoonRayLightShaderNode_IntensityLightFilter'
        layout.operator("node.add_moonray_node", text="Rod Light Filter").type = 'MoonRayLightShaderNode_RodLightFilter'
        layout.operator("node.add_moonray_node", text="Vdb Light Filter").type = 'MoonRayLightShaderNode_VdbLightFilter'

class MoonRayLightShaderNodeMenu_Output(bpy.types.Menu):
    bl_idname = "NODE_MT_lightshader_node_add_moonray_output"
    bl_label = "Add MoonRay Node"

    def draw(self, context):
        layout = self.layout
        layout.operator("node.add_moonray_node", text="MoonRay Light Output").type = 'MoonRayLightShaderNode_Output'

# Compositor Nodes

class MoonRayCompNodeMenu(bpy.types.Menu):
    bl_idname = "NODE_MT_comp_node_add_moonray"
    bl_label = "MoonRay"

    def draw(self, context):
        layout = self.layout
        layout.menu("NODE_MT_comp_node_add_moonray_displayfilter", text="Display Filter")

class MoonRayCompNodeMenu_DisplayFilter(bpy.types.Menu):
    bl_idname = "NODE_MT_comp_node_add_moonray_displayfilter"
    bl_label = "Display Filter"

    def draw(self, context):
        layout = self.layout
        layout.operator("node.add_moonray_node", text="Blend Display Filter").type = 'MoonRayCompNode_BlendDisplayFilter'
        layout.operator("node.add_moonray_node", text="Clamp Display Filter").type = 'MoonRayCompNode_ClampDisplayFilter'
        layout.operator("node.add_moonray_node", text="Color Correct Display Filter").type = 'MoonRayCompNode_ColorCorrectDisplayFilter'
        layout.operator("node.add_moonray_node", text="Constant Display Filter").type = 'MoonRayCompNode_ConstantDisplayFilter'
        layout.operator("node.add_moonray_node", text="Convolution Display Filter").type = 'MoonRayCompNode_ConvolutionDisplayFilter'
        layout.operator("node.add_moonray_node", text="Discretize Display Filter").type = 'MoonRayCompNode_DiscretizeDisplayFilter'
        layout.operator("node.add_moonray_node", text="Dof Display Filter").type = 'MoonRayCompNode_DofDisplayFilter'
        layout.operator("node.add_moonray_node", text="Halftone Display Filter").type = 'MoonRayCompNode_HalftoneDisplayFilter'
        layout.operator("node.add_moonray_node", text="Image Display Filter").type = 'MoonRayCompNode_ImageDisplayFilter'
        layout.operator("node.add_moonray_node", text="Op Display Filter").type = 'MoonRayCompNode_OpDisplayFilter'
        layout.operator("node.add_moonray_node", text="Over Display Filter").type = 'MoonRayCompNode_OverDisplayFilter'
        layout.operator("node.add_moonray_node", text="Ramp Display Filter").type = 'MoonRayCompNode_RampDisplayFilter'
        layout.operator("node.add_moonray_node", text="Remap Display Filter").type = 'MoonRayCompNode_RemapDisplayFilter'
        layout.operator("node.add_moonray_node", text="RgbToFloat Display Filter").type = 'MoonRayCompNode_RgbToFloatDisplayFilter'
        layout.operator("node.add_moonray_node", text="RgbToHsv Display Filter").type = 'MoonRayCompNode_RgbToHsvDisplayFilter'
        layout.operator("node.add_moonray_node", text="Shadow Display Filter").type = 'MoonRayCompNode_ShadowDisplayFilter'
        layout.operator("node.add_moonray_node", text="TangentSpace Display Filter").type = 'MoonRayCompNode_TangentSpaceDisplayFilter'
        layout.operator("node.add_moonray_node", text="Toon Display Filter").type = 'MoonRayCompNode_ToonDisplayFilter'


classes = [MoonRayShaderNodeMenu_Shader, MoonRayShaderNodeMenu_Map, MoonRayShaderNodeMenu_Output, MoonRayShaderNodeMenu_Displacement, MoonRayShaderNodeMenu_Normal, MoonRayShaderNodeMenu,
           MoonRayCompNodeMenu, MoonRayCompNodeMenu_DisplayFilter, MoonRayLightShaderNodeMenu, MoonRayLightShaderNodeMenu_LightFilter, MoonRayLightShaderNodeMenu_Output
           ]

def shader_menu_draw(self, context):
    if context.scene.render.engine == MoonRayRenderEngine.bl_idname:
        layout = self.layout
        
        if context.active_object and context.active_object.type == 'LIGHT':
            layout.menu("NODE_MT_lightshader_node_add_moonray", text="MoonRay")
        else:
            layout.menu("NODE_MT_shader_node_add_moonray", text="MoonRay")

def comp_menu_draw(self, context):
    if context.scene.render.engine == MoonRayRenderEngine.bl_idname:
        layout = self.layout
        layout.menu("NODE_MT_comp_node_add_moonray", text="MoonRay")

# Register the custom shader node
def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.NODE_MT_shader_node_add_all.append(shader_menu_draw)
    bpy.types.NODE_MT_compositor_node_add_all.append(comp_menu_draw)

def unregister():
    bpy.types.NODE_MT_shader_node_add_all.remove(shader_menu_draw)
    bpy.types.NODE_MT_compositor_node_add_all.remove(comp_menu_draw)
    
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)