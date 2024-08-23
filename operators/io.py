import bpy
import os, subprocess
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
    bl_description="Export Dreamworks MoonRay RDL2 (.rdla/.rdlb) file"
    bl_label = "Dreamworks MoonRay RDL2 (.rdla/.rdlb)"
    
    filepath: StringProperty(subtype="FILE_PATH", default="scene.rdla")
    
    def execute(self, context):
        # 1. Export the current Blender scene to a USD file
        usd_filepath = os.path.splitext(self.filepath)[0] + ".usd"
        bpy.ops.wm.usd_export(filepath=usd_filepath)
        print(f"Exported USD file to {usd_filepath}")
        
        # 2. Convert the USD file to RDLA
        rdla_filepath = self.convert_usd_to_rdla(usd_filepath)
        if rdla_filepath:
            print(f"Converted USD to RDLA: {rdla_filepath}")
        else:
            print("Conversion failed.")
            return {'CANCELLED'}
        
        return {'FINISHED'}
    
    def convert_usd_to_rdla(self, usd_filepath):
        # Set up paths
        rdla_filepath = os.path.splitext(usd_filepath)[0] + ".rdla"
        
        # Construct the command to source the setup script and run the conversion
        command = f"source /home/hoske/.mfb/installs/openmoonray/scripts/setup.sh && " \
                  f"/home/hoske/.mfb/installs/openmoonray/bin/hd_usd2rdl -in {usd_filepath} -out {rdla_filepath}"
        
        try:
            # Run the command in a shell
            subprocess.run(command, shell=True, check=True, executable="/bin/bash")
            return rdla_filepath
        except subprocess.CalledProcessError as e:
            print(f"Error during USD to RDLA conversion: {e}")
            return None
    
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