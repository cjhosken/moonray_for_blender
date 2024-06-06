import bpy
from ...moonray_bl_nodes_base import MoonRayShaderNode

class MoonRayWorldOutputNode(MoonRayShaderNode):
    bl_label = 'MoonRay World Output'
    bl_idname = "MoonRay_WorldOutputNode"
    renderman_node_type = 'output'
    node_tree = None
    new_links = []    

    def init(self, context):
        self._init_inputs()   

    def _init_inputs(self):
        input = self.inputs.new('MoonRayNodeSocketBxdf', 'Surface')
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
            if (hasattr(link.from_socket, "moonray_type")):
                if link.from_socket.moonray_type != link.to_socket.moonray_type:
                    node_tree = self.id_data
                    try:
                        node_tree.links.remove(link)
                    except:
                        pass
            else:
                link.is_valid = False


        
        self.new_links.clear()