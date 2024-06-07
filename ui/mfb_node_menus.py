import bpy

class MoonRayShaderNodeMenu(bpy.types.Menu):
    bl_idname = "NODE_MT_shader_node_add_moonray"
    bl_label = "Add MoonRay Node"

    def draw(self, context):
        layout = self.layout
        layout.menu("NODE_MT_shader_node_add_moonray_basic", text="Basic")
        layout.menu("NODE_MT_shader_node_add_moonray_output", text="Output")

class MoonRayShaderNodeMenu_Basic(bpy.types.Menu):
    bl_idname = "NODE_MT_shader_node_add_moonray_basic"
    bl_label = "Add MoonRay Node"

    def draw(self, context):
        layout = self.layout
        layout.operator("node.add_node", text="MoonRay Node").type = 'MoonRayShaderNode_Base'

class MoonRayShaderNodeMenu_Output(bpy.types.Menu):
    bl_idname = "NODE_MT_shader_node_add_moonray_output"
    bl_label = "Add MoonRay Node"

    def draw(self, context):
        layout = self.layout
        layout.operator("node.add_node", text="MoonRay Output").type = 'MoonRayShaderNode_Output'


classes = [MoonRayShaderNodeMenu_Basic, MoonRayShaderNodeMenu_Output, MoonRayShaderNodeMenu]


def shader_menu_draw(self, context):
    layout = self.layout
    # Create a dropdown menu for adding nodes
    layout.menu("NODE_MT_shader_node_add_moonray", text="MoonRay")

# Register the custom shader node
def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.NODE_MT_shader_node_add_all.append(shader_menu_draw)

def unregister():
    bpy.types.NODE_MT_shader_node_add_all.remove(shader_menu_draw)
    
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)