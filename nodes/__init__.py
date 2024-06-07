import bpy
from bpy.types import NodeTree, Node, NodeSocket
from nodeitems_utils import NodeItem

from . import shaders
# Register the custom shader node
def register():
    shaders.register()

def unregister():
    shaders.unregister()