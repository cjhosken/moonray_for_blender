import bpy
from bpy.props import *

from .mfb_panel import MOONRAY_PT_Panel

class MOONRAY_PT_ObjectPanel(MOONRAY_PT_Panel):
    bl_label = "MoonRay"
    bl_idname = "MOONRAY_PT_ObjectPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.object and context.object.type != 'LIGHT'

    def draw(self, context):
        layout = self.layout
        obj = context.object
        scene = context.scene
        moonray = scene.moonray
        
        layout.prop(obj.moonray, "is_light")

        layout.prop_search(obj.moonray, "light_set", moonray.light_sets, "items", text="Light Set", results_are_suggestions=True)
        layout.prop_search(obj.moonray, "shadow_set", moonray.shadow_sets, "items", text="Shadow Set", results_are_suggestions=True)
        layout.prop_search(obj.moonray, "shadowreceiver_set", moonray.shadowreceiver_sets, "items", text="Shadow Receiver Set", results_are_suggestions=True)
        layout.prop(obj.moonray, "shadowreceiver_set_input", text="Shadow Receiver Sets")
        layout.prop(obj.moonray, "trace_set_input", text="Trace Sets")


classes = [MOONRAY_PT_ObjectPanel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)