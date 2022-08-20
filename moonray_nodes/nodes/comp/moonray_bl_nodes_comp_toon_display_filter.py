import bpy
from bpy.props import *
from ...moonray_bl_nodes_base import MoonRayCompNode

class MoonRayCompToonDisplayFilterNode(MoonRayCompNode):
    bl_label = 'MoonRay Toon Display Filter'
    bl_idname = "MoonRay_CompToonDisplayFilterNode"
    renderman_node_type = 'filter'
    node_tree = None
    new_links = []    

    num_cels: IntProperty(default=2)
    ambient: FloatVectorProperty(subtype="COLOR")

    ink_depth_thresh: FloatProperty(default=0.01)
    ink_normal_thresh: FloatProperty(default=0)
    ink_normal_scale: FloatProperty(default=1)

    def update_on(self, context):
        self.update()

    def init(self, context):
        self._init_inputs()
        self._init_outputs()

    def _init_inputs(self):
        input = self.add_input("NodeSocketColor", "Diffuse", [1.0, 1.0, 1.0, 1.0])
        input.hide_value = True
        input = self.add_input("NodeSocketColor","Glossy", [1.0, 1.0, 1.0, 1.0])
        input.hide_value = True
        input = self.add_input("NodeSocketColor","Albedo", [1.0, 1.0, 1.0, 1.0])
        input.hide_value = True
        input = self.add_input("NodeSocketColor", "Depth", [1.0, 1.0, 1.0, 1.0])
        input.hide_value = True
        input = self.add_input("NodeSocketColor","Normal", [1.0, 1.0, 1.0, 1.0])
        input.hide_value = True

    def _init_outputs(self):
        self.outputs.new("NodeSocketColor", 'Image')

    def draw_buttons(self, context, layout):
        layout.prop(self, "num_cels", text="Num Cels")
        layout.prop(self, "ambient", text="Ambient")

        layout.prop(self, "ink_depth_thresh", text="Ink Depth Threshold")
        layout.prop(self, "ink_normal_thresh", text="Ink Normal Threshold")
        layout.prop(self, "ink_normal_scale", text="Ink Normal Scale")

    def insert_link(self, link):
        if link in self.new_links:
            pass
        else:
            self.new_links.append(link)