import bpy
from bpy.props import *

class MOONRAY_OT_ImportRDL(bpy.types.Operator):
    bl_idname = "moonray.import_rdl"
    bl_description=""
    bl_label = "Dreamworks MoonRay RDL2 (.rdla/.rdlb)"
    
    filepath: StringProperty(subtype="FILE_PATH")
    
    def execute(self, context):
        # Your import logic here
        print(f"Importing from {self.filepath}")
        return {'FINISHED'}
    
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

# Define the export operator
class MOONRAY_OT_ExportRDL(bpy.types.Operator):
    bl_idname = "moonray.export_rdl"
    bl_description=""
    bl_label = "Dreamworks MoonRay RDL2 (.rdla/.rdlb)"
    
    filepath: StringProperty(subtype="FILE_PATH")
    
    def execute(self, context):
        # Your export logic here
        print(f"Exporting to {self.filepath}")
        return {'FINISHED'}
    
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
    
classes = [MOONRAY_OT_ImportRDL, MOONRAY_OT_ExportRDL]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)