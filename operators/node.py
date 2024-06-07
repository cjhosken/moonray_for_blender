import bpy

class NODE_OT_add_moonray_node(bpy.types.Operator):
    bl_idname = "node.add_moonray_node"
    bl_label = "Add MoonRay Node"
    
    type: bpy.props.StringProperty()
    
    def execute(self, context):
        bpy.ops.node.add_node(
            'INVOKE_DEFAULT',
            type=self.type,
            use_transform=True
        )
        return {'FINISHED'}

classes = [NODE_OT_add_moonray_node]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)