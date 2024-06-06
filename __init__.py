#  MoonRay for Blender is a render engine addon which allows users to utilise Dreamwork's MoonRay Production Renderer inside of Blender.
#  Copyright 2024 Christopher Hosken
# 
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

bl_info = {
    "name" : "MoonRay For Blender",
    "author" : "Christopher Hosken",
    "version" : (0, 0, 1),
    "blender" : (4, 1, 0),
    "description" : "Dreamworks' MoonRay Production Renderer integration",
    "warning" : "This Addon is currently under development",
    "support": "COMMUNITY",
    "doc_url": "https://github.com/Christopher-Hosken/moonray_for_blender/wiki",
    "tracker_url": "https://github.com/Christopher-Hosken/moonray_for_blender/issues",
    "category" : "Render"
}

from . import engine, properties, ui, nodes

def register():
    engine.register()
    properties.register()
    ui.register()
    nodes.register()

def unregister():
    nodes.unregister()
    ui.unregister()
    properties.unregister()
    engine.unregister()