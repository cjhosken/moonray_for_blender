import bpy
from ..operators.io import MOONRAY_OT_ImportRDL, MOONRAY_OT_ExportRDL

# Function to append the import operator to the file menu
def menu_func_import(self, context):
    self.layout.operator(MOONRAY_OT_ImportRDL.bl_idname)

# Function to append the export operator to the file menu
def menu_func_export(self, context):
    self.layout.operator(MOONRAY_OT_ExportRDL.bl_idname)

def register():
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

def unregister():
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)