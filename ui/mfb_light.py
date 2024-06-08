import bpy

from .mfb_panel import MOONRAY_PT_Panel

class MOONRAY_LIGHT_PT_light(MOONRAY_PT_Panel):
    """Physical light sources"""
    bl_label = "Light"
    bl_context = 'data'

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.light
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene

        moonray = scene.moonray

        light = context.light

        layout.prop(light.moonray, "type", expand=True)

        layout.use_property_split = True
        layout.use_property_decorate = False

        main_col = layout.column()

        main_col.prop(light, "color")
        main_col.prop(light.moonray, "texture")
        main_col.prop(light, "energy")
        main_col.separator()

        main_col.prop(light.moonray, "visible")
        main_col.prop(light.moonray, "motion_blur")
        
        layout.prop_search(light.moonray, "lightfilter_set", moonray.lightfilter_sets, "items", text="Light Filter Set", results_are_suggestions=True)
        layout.prop(light.moonray, "light_set_input", text="Light Sets")
        layout.prop(light.moonray, "shadow_set_input", text="Shadow Sets")
        

classes = [MOONRAY_LIGHT_PT_light]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)