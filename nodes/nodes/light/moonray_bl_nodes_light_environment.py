import bpy
from bpy.props import *
from ...moonray_bl_nodes_base import MoonRayShaderNode

class MoonRayLightEnvironmentNode(MoonRayShaderNode):
    bl_label = 'MoonRay Env Light'
    bl_idname = "MoonRay_EnvLightNode"
    renderman_node_type = 'light'
    node_tree = None
    new_links = []    

    def update_on(self, context):
        self.update()

    on : BoolProperty(
        name="On",
        default=True,
        description="toggle the light",
        update = update_on
    )

    def init(self, context):
        self._init_inputs()
        self._init_outputs()

    def _init_inputs(self):
        self.add_input("NodeSocketColor", "Color", [1.0, 1.0, 1.0, 1.0])
        self.add_input("NodeSocketFloat","Intensity", 1.0)
        self.add_input("NodeSocketFloat","Exposure", 1.0)

    def _init_outputs(self):
        self.outputs.new("MoonRayNodeSocketLight", 'Light')

    def draw_buttons(self, context, layout):
        layout.prop(self, "on", text="On")

    def insert_link(self, link):
        if link in self.new_links:
            pass
        else:
            self.new_links.append(link)