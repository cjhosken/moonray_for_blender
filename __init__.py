# Copyright 2022 Christopher Hosken
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import bpy
from bpy.utils import register_class, unregister_class

bl_info = {
    "name" : "MoonRay Render Engine",
    "author" : "Christopher Hosken",
    "description" : "",
    "blender" : (3, 2, 1),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Render"
}

class MoonRayRender(bpy.types.RenderEngine):
    bl_idname = "MOONRAY"
    bl_label = "MoonRay"
    bl_use_preview = True
    bl_use_texture_preview = False
    bl_use_shading_nodes_custom = False

    def __init__(self):
        pass

    def __del__(self):
        pass

    def render(self, depsgraph):
        pass

    def view_update(self, context, depsgraph):
        pass

    def view_draw(self, context, depsgraph):
        pass

from .preferences import classes as preferences_classes

classes = [MoonRayRender] + preferences_classes

from . import moonray_ui
from . import moonray_nodes

def register():
    for cls in classes:
        register_class(cls)
    moonray_ui.register()
    moonray_nodes.register()

def unregister():
    for cls in classes:
        unregister_class(cls)
    moonray_ui.unregister()
    moonray_nodes.unregister()
