import bpy
import os, subprocess
from bpy.props import *
        
# Define the export operator
class MOONRAY_OT_ExportRDL(bpy.types.Operator):
    bl_idname = "moonray.export_rdl"
    bl_description="Export Dreamworks MoonRay RDL2 (.rdla/.rdlb) file"
    bl_label = "Export Dreamworks MoonRay RDL2 (.rdla/.rdlb)"
    
    filepath: StringProperty(subtype="FILE_PATH", default=os.path.join(os.path.expanduser("~"), "scene.rdla"))
    
    filter_glob: StringProperty(
        default="*.rdla;*.rdlb",
        options={'HIDDEN'},
    )

    export_selection_only: BoolProperty(
        name="Export Selection Only",
        description="Export only the selected objects",
        default=False
    )

    export_visible_only: BoolProperty(
        name="Export Visible Only",
        description="Export only the visible objects",
        default=False
    )

    export_animation: BoolProperty(
        name="Export Animation",
        description="Export the animation",
        default=False
    )

    export_materials: BoolProperty(
        name="Export Materials",
        description="Include materials in the .rdla/.rdlb export",
        default=True
    )

    export_lights: BoolProperty(
        name="Export Lights",
        description="Include lights in the .rdla/.rdlb export",
        default=True
    )

    export_hair: BoolProperty(
        name="Export Hair",
        description="Include hair in the .rdla/.rdlb export",
        default=True
    )

    export_cameras: BoolProperty(
        name="Export Cameras",
        description="Include cameras in the .rdla/.rdlb export",
        default=True
    )

    keep_usd : BoolProperty(
        name="Export USD",
        description="Export a .usd file alongisde the .rdla/.rdlb file.",
        default=True
    )

    def execute(self, context):
        print(self.filepath)
        if len(os.path.basename(self.filepath)) < 1:
            return {"FINISHED"}
        
        # Export the current Blender scene to a USD file
        usd_filepath = os.path.splitext(self.filepath)[0] + ".usd"
        is_rdla = os.path.splitext(self.filepath)[1] == ".rdla"

        bpy.ops.wm.usd_export(filepath=usd_filepath, 
                              selected_objects_only=self.export_selection_only, 
                              visible_objects_only=self.export_visible_only,
                              export_animation=self.export_animation,
                              export_materials=False
                              )
        
        # https://docs.blender.org/api/current/bpy.ops.wm.html

        print(f"Exported USD file to {usd_filepath}")
        
        # Convert the USD file to RDLA/RDLB
        rdla_filepath = self.convert_usd_to_rdla(usd_filepath, is_rdla)
        if rdla_filepath:
            print(f"Converted USD to RDLA: {rdla_filepath}")
            # Delete the temporary USD file
            try:
                if (not self.keep_usd):
                    os.remove(usd_filepath)
                    print(f"Deleted temporary USD file: {usd_filepath}")
            except OSError as e:
                print(f"Error deleting USD file: {e}")
        else:
            print("Conversion failed.")
            return {'CANCELLED'}
        
        return {'FINISHED'}
    
    def convert_usd_to_rdla(self, usd_filepath, is_rdla=False):
        # Set up paths
        extension = ".rdla" if is_rdla else ".rdlb"

        rdla_filepath = os.path.splitext(usd_filepath)[0] + extension
        
        # Construct the command to source the setup script and run the conversion
        command = f'source {os.path.join(os.path.expanduser("~"), ".mfb/installs/openmoonray/scripts/setup.sh")} && ' \
                  f'{os.path.join(os.path.expanduser("~"), ".mfb/installs/openmoonray/bin/hd_usd2rdl")} -in {usd_filepath} -out {rdla_filepath}'
        
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
    
classes = [MOONRAY_OT_ExportRDL]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)