from . import sets
from . import attribute


def register():
    attribute.register()
    sets.register()

def unregister():
    attribute.unregister()
    sets.unregister()