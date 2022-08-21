import bpy
import re
import time
from bpy.props import *

__MOONRAY_SOCKETS__ = [
    # type, , name, color, default
    ("bxdf", "Bxdf", (1.0, 1.0, 1.0, 1.0), StringProperty("")),
    ("light", "Light", (1.0, 1.0, 1.0, 1.0), StringProperty("")),
]

class MoonRaySocket(bpy.types.NodeSocket):
    name = "MoonRaySocket"
    bl_idname = "MoonRayNodeSocket"
    type = "CUSTOM"
    color = (1.0, 1.0, 1.0, 1.0)
    socket_label = "None"
    default_value = None
    is_hidden = False

    def draw(self, context, layout, node, text):
        if not (self.is_hidden):
            layout.label(text=self.socket_label)
    
    def draw_color(self, context,node):
        return self.color

def socket_is_equal(from_socket, to_socket):
    return (from_socket.type == to_socket.type)

classes = []

def register_sockets():
    for ms in __MOONRAY_SOCKETS__:
        socket_type = ms[0]
        socket_name = ms[1]

        socket = type(f"MoonRayNodeSocket{socket_name}", (MoonRaySocket,), {})
        socket.name = f"MoonRaySocket{socket_name}"
        socket.bl_idname = f"MoonRayNodeSocket{socket_name}"
        socket.type = socket_type
        socket.socket_label = socket_name
        socket.color = ms[2]

        socket.default_value : ms[3]

        classes.append(socket)