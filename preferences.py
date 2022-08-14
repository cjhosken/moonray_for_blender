import bpy
from bpy.props import FloatVectorProperty

class MoonRayPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        layout = self.layout
        col = layout.column()

def get_user_prefs(context=None):
    if not context:
        context = bpy.context

    if hasattr(context, "user_preferences"):
        prefs = context.user_preferences.addons[__package__]
    elif hasattr(context, "preferences"):
        prefs = context.preferences.addons[__package__]
    if prefs:
        return prefs.preferences
    return None