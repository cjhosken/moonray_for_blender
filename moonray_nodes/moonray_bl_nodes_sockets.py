import bpy
import re
import time
from bpy.props import *

class MoonRaySocket:
    name = "MoonRaySocket"
    bl_idname = "MoonRayNodeSocket"
    type = "CUSTOM"
    color = (1.0, 1.0, 1.0, 1.0)
    is_hidden = False
    socket_label = "None"

class MoonRaySocketBxdf(MoonRaySocket, bpy.types.NodeSocket):
    name = "MoonRaySocketBxdf"
    bl_idname = "MoonRayNodeSocketBxdf"
    type = "BXDF"
    socket_label = "Bxdf"
    color = (0.0, 1.0, 1.0, 1.0)

    default_value : StringProperty("")

    def draw(self, context, layout, node, text):
        if not (self.is_hidden):
            layout.label(text=self.socket_label)

    def draw_color(self, context,node):
        return self.color

class MoonRaySocketLight(MoonRaySocket, bpy.types.NodeSocket):
    name = "MoonRaySocketLight"
    bl_idname = "MoonRayNodeSocketLight"
    type = "LIGHT"
    socket_label = "Light"
    color = (1.0, 1.0, 0.1, 1.0)

    default_value : StringProperty("")

    def draw(self, context, layout, node, text):
        if not (self.is_hidden):
            layout.label(text=self.socket_label)

    def draw_color(self, context,node):
        return self.color

def socket_is_equal(from_socket, to_socket):
    return (from_socket.type == to_socket.type)

class MoonRaySocketDisplayFilter(MoonRaySocket, bpy.types.NodeSocket):
    name = "MoonRaySocketDF"
    bl_idname = "MoonRayNodeSocketDF"
    type = "DISPLAYFILTER"
    socket_label = "Display Filter"
    color = (1.0, 1.0, 0.1, 1.0)

    default_value : StringProperty("")

    def draw(self, context, layout, node, text):
        if not (self.is_hidden):
            layout.label(text=self.socket_label)

    def draw_color(self, context,node):
        return self.color

def socket_is_equal(from_socket, to_socket):
    return (from_socket.type == to_socket.type)



classes = [MoonRaySocketBxdf,MoonRaySocketLight, MoonRaySocketDisplayFilter]