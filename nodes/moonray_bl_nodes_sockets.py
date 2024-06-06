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
    bl_label = "MoonRaySocket"
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

def register_sockets():
    classes = []
    for ms in __MOONRAY_SOCKETS__:
        socket_type, socket_name, color, default_prop = ms

        socket_class = type(
            f"MoonRayNodeSocket{socket_name}",
            (MoonRaySocket,),
            {
                "bl_label": f"MoonRaySocket{socket_name}",
                "bl_idname": f"MoonRayNodeSocket{socket_name}",
                "type": socket_type,
                "socket_label": socket_name,
                "color": color,
                "default_value": default_prop,
            }
        )


        classes.append(socket_class)
    return classes
