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
    ('float', 'Float', bpy.types.NodeSocketFloat, (0.5, 0.5, 0.5, 1.0), False,
        {
            'default_value': FloatProperty(update=update_func),
        }
    ),
    ('int', 'Int', bpy.types.NodeSocketInt, (1.0, 1.0, 1.0, 1.0), False,
        {
            'default_value': IntProperty(update=update_func),
        }
    ),
        ('bxdf', 'Bxdf', bpy.types.NodeSocketString, (0.25, 1.0, 0.25, 1.0), True,
        {
            'default_value': StringProperty(default=''),
        }
    ),   
        ('color', 'Color', bpy.types.NodeSocketColor, (1.0, 1.0, .5, 1.0), False,
        {
            'default_value': FloatVectorProperty(size=3, subtype="COLOR", update=update_func),
        }
    ), 
]

__MOONRAY_TYPES_SOCKET_INTERFACES__ =[
    ('float', 'Float', bpy.types.NodeSocketInterfaceFloat, (0.5, 0.5, 0.5, 1.0), False,
        {
            'default_value': FloatProperty() 
        }
    ),
    ('int', 'Int', bpy.types.NodeSocketInterfaceInt, (1.0, 1.0, 1.0, 1.0), False,
        {
            'default_value': IntProperty()
        }
    ),    
    ('bxdf', 'Bxdf', bpy.types.NodeSocketInterfaceString, (0.25, 1.0, 0.25, 1.0), True,
        {
            'default_value': StringProperty(default=''),
        }
    ),       
    ('color', 'Color', bpy.types.NodeSocketInterfaceColor, (1.0, 1.0, .5, 1.0), False,
        {
            'default_value': FloatVectorProperty(size=3, subtype="COLOR", update=update_func),
        }
    ),      
]

class MoonRaySocket:
    ui_open: BoolProperty(name='UI Open', default=True)

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
            
        mat = getattr(context, 'material')
        if mat:
            return

class MoonRaySocketInterface:

    def draw_color(self, context):
        return (0.25, 1.0, 0.25, 1.0)

    def draw(self, context, layout):
        layout.label(text=self.name)

    def from_socket(self, node, socket):
        pass


    def init_socket(self, node, socket, data_path):
        pass

classes = []

def register_socket_classes():
    global classes

    def draw_color(self, context, node):
        return self.socket_color

    for socket_info in __MOONRAY_TYPES_SOCKETS__:
        label = socket_info[1]
        typename = 'MoonRayNodeSocket%s' % label
        ntype = type(typename, (socket_info[2], MoonRaySocket,), {})
        ntype.bl_label = 'MoonRay %s Socket' % label
        ntype.bl_idname = typename
        if "__annotations__" not in ntype.__dict__:
            setattr(ntype, "__annotations__", {})        
        ntype.draw_color = draw_color
        ntype.socket_color = socket_info[3]
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
        label = socket_info[1]
        typename = 'MoonRayNodeSocketInterface%s' % label
        ntype = type(typename, (socket_info[2], MoonRaySocketInterface,), {})        
        # bl_socket_idname needs to correspond to the MoonRayNodeSocket class
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