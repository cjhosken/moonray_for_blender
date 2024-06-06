import bpy
from ...moonray_bl_nodes_base import MoonRayShaderNode

class MoonRayLightOutputNode(MoonRayShaderNode):
    bl_label = 'MoonRay Light Output'
    bl_idname = "MoonRay_LightOutputNode"
    renderman_node_type = 'output'
    node_tree = None
    new_links = []    

    def init(self, context):
        self._init_inputs()   

    def _init_inputs(self):
        input = self.inputs.new('MoonRayNodeSocketLight', 'Light')
        input.hide_value = True

    def draw_buttons(self, context, layout):
        return

    def draw_buttons_ext(self, context, layout):
        return

    def insert_link(self, link):
        if link in self.new_links:
            pass
        else:
            self.new_links.append(link)