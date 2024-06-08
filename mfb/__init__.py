from . import sets
from . import userdata
from . import deep
from . import meta
from . import attributes
from . import render_output

def register():
    meta.register()
    deep.register()
    attributes.register()
    render_output.register()
    userdata.register()
    sets.register()

def unregister():
    userdata.unregister()
    sets.unregister()
    render_output.unregister()
    attributes.unregister()
    deep.unregister()
    meta.unregister()