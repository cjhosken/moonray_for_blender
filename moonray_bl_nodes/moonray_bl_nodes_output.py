import bpy
from .moonray_bl_nodes_base import MoonRayShadingNode

class MoonRayOutputNode(MoonRayShadingNode):
    bl_label = 'MoonRay Output'
    bl_idname = "MoonRay_OutputNode"
    renderman_node_type = 'output'
    bl_icon = 'MATERIAL'
    node_tree = None
    new_links = []    

    def init(self, context):
        self._init_inputs()   

    def _init_inputs(self):
        input = self.inputs.new('MoonRayNodeSocketBxdf', 'Bxdf')
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


    def update(self):
        for link in self.new_links:
            pass

        
        self.new_links.clear()