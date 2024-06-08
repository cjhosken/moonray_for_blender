import bpy
from bpy.props import *

from .mfb_panel import MOONRAY_PT_Panel


class MOONRAY_UL_SetList(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        self.use_filter_show = True
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.prop(item, "name", text="", emboss=False, icon_value=icon)
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon_value=icon)

class MOONRAY_PT_ViewLayerPanel(MOONRAY_PT_Panel):
    bl_label = "MoonRay"
    bl_idname = "MOONRAY_PT_ViewLayerPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "view_layer"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        moonray = scene.moonray

        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.prop(moonray.output, "denoise")
        layout.prop(moonray.output, "denoiser_input")
        layout.prop(moonray.output, "display_filter")

class MOONRAY_MT_ViewLayer_SetsPanel(MOONRAY_PT_Panel):
    bl_label = "Sets"
    bl_idname = "MOONRAY_PT_ViewLayer_SetsPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "view_layer"
    bl_parent_id = "MOONRAY_PT_ViewLayerPanel"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

class MOONRAY_MT_ViewLayer_CryptomattePanel(MOONRAY_PT_Panel):
    bl_label = "Cryptomattes"
    bl_idname = "MOONRAY_PT_ViewLayer_CryptomattePanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "view_layer"
    bl_parent_id = "MOONRAY_PT_ViewLayerPanel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        moonray = scene.moonray

        layout.use_property_split = True
        layout.use_property_decorate = False
        
        layout.prop(moonray.output, "cryptomatte_depth")
        layout.prop(moonray.output, "cryptomatte_enable_refract")
        layout.prop(moonray.output, "cryptomatte_output_beauty")
        layout.prop(moonray.output, "cryptomatte_output_normals")
        layout.prop(moonray.output, "cryptomatte_output_p0")
        layout.prop(moonray.output, "cryptomatte_output_positions")
        layout.prop(moonray.output, "cryptomatte_output_refn")
        layout.prop(moonray.output, "cryptomatte_output_refp")
        layout.prop(moonray.output, "cryptomatte_output_uv")
        layout.prop(moonray.output, "cryptomatte_support_resume_render")

class MOONRAY_MT_ViewLayer_LightFilterPanel(MOONRAY_PT_Panel):
    bl_label = "Light Filters"
    bl_idname = "MOONRAY_PT_ViewLayer_LightFilterPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "view_layer"
    bl_parent_id = "MOONRAY_PT_ViewLayerPanel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        moonray = scene.moonray

        layout.use_property_split = True
        layout.use_property_decorate = False



class MOONRAY_MT_ViewLayer_LightSetsPanel(MOONRAY_PT_Panel):
    bl_label = "Lights"
    bl_idname = "MOONRAY_PT_ViewLayer_LightSetsPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "view_layer"
    bl_parent_id = "MOONRAY_PT_ViewLayer_SetsPanel"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False


        light_sets = context.scene.moonray.light_sets
        lightfilter_sets = context.scene.moonray.lightfilter_sets

        layout.label(text="Light Sets")
        row = layout.row()
        col = row.column()
        col.template_list("MOONRAY_UL_SetList", "light_sets", light_sets,
                          "items", light_sets, "index", rows=3)

        col = row.column()
        sub = col.column(align=True)
        sub.operator("moonray.add_light_set", icon='ADD', text="")
        sub.operator("moonray.remove_light_set", icon='REMOVE', text="")
        sub.separator()

        # Light Filter Sets
        layout.label(text="Light Filter Sets")
        row = layout.row()
        col = row.column()
        col.template_list("MOONRAY_UL_SetList", "lightfilter_sets", lightfilter_sets,
                          "items", lightfilter_sets, "index", rows=3)

        col = row.column()
        sub = col.column(align=True)
        sub.operator("moonray.add_lightfilter_set", icon='ADD', text="")
        sub.operator("moonray.remove_lightfilter_set", icon='REMOVE', text="")
        sub.separator()  

class MOONRAY_MT_ViewLayer_ShadowSetsPanel(MOONRAY_PT_Panel):
    bl_label = "Shadows"
    bl_idname = "MOONRAY_PT_ViewLayer_ShadowSetsPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "view_layer"
    bl_parent_id = "MOONRAY_PT_ViewLayer_SetsPanel"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        shadow_sets = context.scene.moonray.shadow_sets
        shadowreceiver_sets = context.scene.moonray.shadowreceiver_sets
        # Shadow Set

        layout.label(text="Shadow Sets")
        row = layout.row()
        col = row.column()
        col.template_list("MOONRAY_UL_SetList", "shadow_sets", shadow_sets,
                          "items", shadow_sets, "index", rows=3)

        col = row.column()
        sub = col.column(align=True)
        sub.operator("moonray.add_shadow_set", icon='ADD', text="")
        sub.operator("moonray.remove_shadow_set", icon='REMOVE', text="")
        sub.separator()

        # Shadow Receiver Set

        layout.label(text="Shadow Receiver Sets")
        row = layout.row()
        col = row.column()
        col.template_list("MOONRAY_UL_SetList", "shadowreceiver_sets", shadowreceiver_sets,
                          "items", shadowreceiver_sets, "index", rows=3)

        col = row.column()
        sub = col.column(align=True)
        sub.operator("moonray.add_shadowreceiver_set", icon='ADD', text="")
        sub.operator("moonray.remove_shadowreceiver_set", icon='REMOVE', text="")
        sub.separator()   

class MOONRAY_MT_ViewLayer_TraceSetsPanel(MOONRAY_PT_Panel):
    bl_label = "Trace"
    bl_idname = "MOONRAY_PT_ViewLayer_TraceSetsPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "view_layer"
    bl_parent_id = "MOONRAY_PT_ViewLayer_SetsPanel"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        trace_sets = context.scene.moonray.trace_sets

        layout.label(text="Trace Sets")
        row = layout.row()
        col = row.column()
        col.template_list("MOONRAY_UL_SetList", "trace_sets", trace_sets,
                          "items", trace_sets, "index", rows=3)

        col = row.column()
        sub = col.column(align=True)
        sub.operator("moonray.add_trace_set", icon='ADD', text="")
        sub.operator("moonray.remove_trace_set", icon='REMOVE', text="")
        sub.separator()


classes = [MOONRAY_UL_SetList, MOONRAY_PT_ViewLayerPanel, MOONRAY_MT_ViewLayer_SetsPanel, MOONRAY_MT_ViewLayer_LightSetsPanel, MOONRAY_MT_ViewLayer_ShadowSetsPanel, MOONRAY_MT_ViewLayer_TraceSetsPanel, MOONRAY_MT_ViewLayer_CryptomattePanel, MOONRAY_MT_ViewLayer_LightFilterPanel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)