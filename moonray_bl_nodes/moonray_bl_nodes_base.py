import bpy
from bpy.props import EnumProperty, StringProperty, CollectionProperty, BoolProperty, PointerProperty
from nodeitems_utils import NodeCategory

class MoonRayShadingNode(bpy.types.ShaderNode):
    bl_label = 'Output'
    @classmethod
    def poll(cls, ntree):
        rd = bpy.context.scene.render
        if rd.engine != 'MOONRAY':
            return False

        if hasattr(ntree, 'bl_idname'):
            return ntree.bl_idname == 'ShaderNodeTree'
        else:
            return True    
        
    def draw_buttons(self, context, layout):
        nt = self.id_data
        mat = context.material

    def update(self):
        for output in self.outputs:
            if not output.is_linked:
                continue
            if len(output.links) < 1:
                continue
            link = output.links[0]
            from_node_type = getattr(link.from_socket, 'moonray_type', None)
            to_node_type = getattr(link.to_socket, 'moonray_type', None)
            if not from_node_type:
                continue            
            if not to_node_type:
                continue            

class MoonRayShaderNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        rd = context.scene.render
        if (rd.engine != "MOONRAY"):
            return False
        return context.space_data.tree_type == "ShaderNodeTree" and context.space_data.shader_type in ["OBJECT", "WORLD"]