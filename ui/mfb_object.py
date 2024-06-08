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



class MOONRAY_PT_Object_UserDataPanel(MOONRAY_PT_Panel):
    bl_label = "User Data"
    bl_idname = "MOONRAY_PT_UserDataPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
    bl_parent_id = "MOONRAY_PT_ObjectPanel"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        user_data = obj.moonray.user_data
        
        row = layout.row()
        row.label(text="Add User Data:")
        row.operator("moonray.add_userdata", text="", icon='ADD')

        for prop in user_data:
            row = layout.row(align=True)
            row.prop(prop, "name", text="")
            if prop.type == 'BOOL':
                row.prop(prop, "value_bool", text="Value")
            elif prop.type == 'COLOR':
                row.prop(prop, "value_color", text="Value")
            elif prop.type == 'FLOAT':
                row.prop(prop, "value_float", text="Value")
            elif prop.type == 'INTEGER':
                row.prop(prop, "value_int", text="Value")
            elif prop.type == 'MAT4F':
                row.prop(prop, "value_mat4f", text="Value")
            elif prop.type == 'STRING':
                row.prop(prop, "value_string", text="Value")
            elif prop.type == 'VEC2F':
                row.prop(prop, "value_vec2f", text="Value")
            elif prop.type == 'VEC3F':
                row.prop(prop, "value_vec3f", text="Value")

            row.operator("moonray.remove_userdata", text="", icon='X').index = user_data[:].index(prop)

    

classes = [MOONRAY_PT_ObjectPanel, MOONRAY_PT_Object_UserDataPanel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)