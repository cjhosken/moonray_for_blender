import bpy
import re
import time
from bpy.props import *

__CYCLES_GROUP_NODES__ = ['ShaderNodeGroup', 'NodeGroupInput', 'NodeGroupOutput']
__SOCKET_HIDE_VALUE__ = ['bxdf', 'projection', 'light', 'integrator', 'struct', 'vstruct'
                        'samplefilter', 'displayfilter']

def update_func(self, context):
    # check if this prop is set on an input
    node = self.node if hasattr(self, 'node') else self

__MOONRAY_TYPES_SOCKETS__ = [
    ('bxdf', 'Bxdf', bpy.types.NodeSocketString, (0.25, 1.0, 0.25, 1.0), True,
        {
            'default_value': StringProperty(default=''),
        }
    ),   
    ('light', 'Light', bpy.types.NodeSocketColor, (1.0, 1.0, .5, 1.0), False,
        {
            'default_value': StringProperty(default=''),
        }
    ), 
]

__MOONRAY_TYPES_SOCKET_INTERFACES__ =[
    ('bxdf', 'Bxdf', bpy.types.NodeSocketInterfaceString, (0.25, 1.0, 0.25, 1.0), True,
        {
            'default_value': StringProperty(default=''),
        }
    ),    
    ('light', 'Light', bpy.types.NodeSocketInterfaceColor, (1.0, 1.0, .5, 1.0), False,
        {
            'default_value': StringProperty(default=''),
        }
    ),
]

class MoonRaySocket:
    def get_pretty_name(self, node):
        if node.bl_idname in __CYCLES_GROUP_NODES__:
            return self.name
        else:
            return self.identifier

    def get_value(self, node):
        if node.bl_idname in __CYCLES_GROUP_NODES__ or not hasattr(node, self.name):
            return self.default_value
        else:
            return getattr(node, self.name)

    def draw_color(self, context, node):
        return (0.25, 1.0, 0.25, 1.0)

    def draw_value(self, context, layout, node):
        layout.prop(node, self.identifier)

    def draw(self, context, layout, node, text):      
        moonray_type = getattr(self, 'moonray_type', '')
        if self.hide and self.hide_value:
            pass
        elif self.hide_value:
            layout.label(text=self.get_pretty_name(node))
        elif self.is_linked or self.is_output:
            layout.label(text=self.get_pretty_name(node))
        elif moonray_type in __SOCKET_HIDE_VALUE__:
            layout.label(text=self.get_pretty_name(node))                        
        elif hasattr(node, self.name):
            layout.prop(node, self.name,
                        text=self.get_pretty_name(node), slider=True)
        else:
            # check if this is an array element
            expr = re.compile(r'.*(\[\d+\])')
            m = expr.match(self.name)
            if m and m.groups():
                group = m.groups()[0]
                coll_nm = self.name.replace(group, '')
                collection = getattr(node, '%s_collection' % coll_nm)
                elem = None
                for e in collection:
                    if e.name == self.name:
                        elem = e
                        break
                if elem:               
                    layout.prop(elem, 'value_%s' % elem.type, text=elem.name, slider=True)
                else:
                    layout.label(text=self.get_pretty_name(node))
            else:
                layout.label(text=self.get_pretty_name(node))      
        mat = getattr(context, 'material')
        if mat:
            return

class MoonRaySocketInterface:

    def draw_color(self, context):
        return (0.25, 1.0, 0.25, 1.0)

    def draw(self, context, layout):
        layout.label(text=self.name)

    def from_socket(self, node, socket):
        if hasattr(self, 'default_value'):
            self.default_value = socket.get_value(node)
        if hasattr(self, 'struct_name'):
            self.struct_name = socket.struct_name         
        if hasattr(self, 'is_texture'):
            self.is_texture = socket.is_texture
        self.name = socket.name


    def init_socket(self, node, socket, data_path):
        time.sleep(.01)
        socket.name = self.name
        if hasattr(self, 'default_value'):
            socket.default_value = self.default_value
        if hasattr(self, 'struct_name'):
            socket.struct_name = self.struct_name   
        if hasattr(self, 'is_texture'):
            socket.is_texture = self.is_texture  

classes = []

def register_socket_classes():
    global classes

    def draw_color(self, context, node):
        return self.socket_color

    for socket_info in __MOONRAY_TYPES_SOCKETS__:
        moonray_type = socket_info[0]
        label = socket_info[1]
        typename = 'MoonRayNodeSocket%s' % label
        ntype = type(typename, (socket_info[2], MoonRaySocket,), {})
        ntype.bl_label = 'MoonRay %s Socket' % label
        ntype.bl_idname = typename
        if "__annotations__" not in ntype.__dict__:
            setattr(ntype, "__annotations__", {})        
        ntype.draw_color = draw_color
        ntype.socket_color = socket_info[3]
        ntype.__annotations__['moonray_type'] = StringProperty(default='%s' % moonray_type)
        if socket_info[4]:
            ntype.__annotations__['hide_value'] = True
        ann_dict = socket_info[5]
        for k, v in ann_dict.items():
            ntype.__annotations__[k] = v

        classes.append(ntype)

def register_socket_interface_classes():
    global classes

    def draw_socket_color(self, context):
        return self.socket_color
    
    for socket_info in __MOONRAY_TYPES_SOCKET_INTERFACES__:
        moonray_type = socket_info[0]
        label = socket_info[1]
        typename = 'MoonRayNodeSocketInterface%s' % label
        ntype = type(typename, (socket_info[2], MoonRaySocketInterface,), {})        
        # bl_socket_idname needs to correspond to the RendermanNodeSocket class
        ntype.bl_socket_idname = 'MoonRayNodeSocket%s' % label
        if "__annotations__" not in ntype.__dict__:
            setattr(ntype, "__annotations__", {})        
        ntype.draw_color = draw_socket_color
        ntype.socket_color = socket_info[3]
        if socket_info[4]:
            ntype.__annotations__['hide_value'] = True        
        ann_dict = socket_info[5]
        for k, v in ann_dict.items():
            ntype.__annotations__[k] = v

        classes.append(ntype)      

def register():

    register_socket_interface_classes()
    register_socket_classes()

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        try:
            bpy.utils.unregister_class(cls)
        except:
            pass