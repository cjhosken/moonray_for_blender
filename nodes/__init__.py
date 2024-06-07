import bpy
from bpy.types import NodeTree, Node, NodeSocket
from nodeitems_utils import NodeItem

from . import shaders
from . import comp
# Register the custom shader node
def register():
    shaders.register()
    comp.register()

def unregister():
    shaders.unregister()
    comp.unregister()