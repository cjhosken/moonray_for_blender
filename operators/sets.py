import bpy

from bpy.props import *

# Operator to add light groups
class MOONRAY_OT_AddLightSet(bpy.types.Operator):
    bl_idname = "moonray.add_light_set"
    bl_label = "Add Light Set"
    bl_description = "Add a new light set to the list"

    def execute(self, context):
        sets = context.scene.moonray.light_sets
        new_item = sets.items.add()
        new_item.name = "Light Set {}".format(len(sets.items))
        sets.index = len(sets.items) - 1
        return {'FINISHED'}
    
class MOONRAY_OT_RemoveLightSet(bpy.types.Operator):
    bl_idname = "moonray.remove_light_set"
    bl_label = "Remove Light Set"
    bl_description = "Remove the selected light set from the list"

    def execute(self, context):
        sets = context.scene.moonray.light_sets
        if sets.items:
            sets.items.remove(sets.index)
            sets.index = min(max(0, sets.index - 1), len(sets.items) - 1)
        return {'FINISHED'}
    

# Operator to add light groups
class MOONRAY_OT_AddLightFilterSet(bpy.types.Operator):
    bl_idname = "moonray.add_lightfilter_set"
    bl_label = "Add Light Filter Set"
    bl_description = "Add a new light filter set to the list"

    def execute(self, context):
        sets = context.scene.moonray.lightfilter_sets
        new_item = sets.items.add()
        new_item.name = "Light Filter Set {}".format(len(sets.items))
        sets.index = len(sets.items) - 1
        return {'FINISHED'}
    
class MOONRAY_OT_RemoveLightFilterSet(bpy.types.Operator):
    bl_idname = "moonray.remove_lightfilter_set"
    bl_label = "Remove Light Filter Set"
    bl_description = "Remove the selected light filter set from the list"

    def execute(self, context):
        sets = context.scene.moonray.lightfilter_sets
        if sets.items:
            sets.items.remove(sets.index)
            sets.index = min(max(0, sets.index - 1), len(sets.items) - 1)
        return {'FINISHED'}
    



# Operator to add light groups
class MOONRAY_OT_AddShadowSet(bpy.types.Operator):
    bl_idname = "moonray.add_shadow_set"
    bl_label = "Add Shadow Set"
    bl_description = "Add a new shadow set to the list"

    def execute(self, context):
        sets = context.scene.moonray.shadow_sets
        new_item = sets.items.add()
        new_item.name = "Shadow Set {}".format(len(sets.items))
        sets.index = len(sets.items) - 1
        return {'FINISHED'}
    
class MOONRAY_OT_RemoveShadowSet(bpy.types.Operator):
    bl_idname = "moonray.remove_shadow_set"
    bl_label = "Remove Shadow Set"
    bl_description = "Remove the selected shadow set from the list"

    def execute(self, context):
        sets = context.scene.moonray.shadow_sets
        if sets.items:
            sets.items.remove(sets.index)
            sets.index = min(max(0, sets.index - 1), len(sets.items) - 1)
        return {'FINISHED'}


# Operator to add light groups
class MOONRAY_OT_AddShadowReceiverSet(bpy.types.Operator):
    bl_idname = "moonray.add_shadowreceiver_set"
    bl_label = "Add Shadow Receiver Set"
    bl_description = "Add a new shadow receiver set to the list"

    def execute(self, context):
        sets = context.scene.moonray.shadowreceiver_sets
        new_item = sets.items.add()
        new_item.name = "Shadow Receiver Set {}".format(len(sets.items))
        sets.index = len(sets.items) - 1
        return {'FINISHED'}
    
class MOONRAY_OT_RemoveShadowReceiverSet(bpy.types.Operator):
    bl_idname = "moonray.remove_shadowreceiver_set"
    bl_label = "Remove Shadow Receiver Set"
    bl_description = "Remove the selected shadow receiver set from the list"

    def execute(self, context):
        sets = context.scene.moonray.shadowreceiver_sets
        if sets.items:
            sets.items.remove(sets.index)
            sets.index = min(max(0, sets.index - 1), len(sets.items) - 1)
        return {'FINISHED'}
    

# Operator to add light groups
class MOONRAY_OT_AddTraceSet(bpy.types.Operator):
    bl_idname = "moonray.add_trace_set"
    bl_label = "Add Trace Set"
    bl_description = "Add a new trace set to the list"

    def execute(self, context):
        sets = context.scene.moonray.trace_sets
        new_item = sets.items.add()
        new_item.name = "Trace Set {}".format(len(sets.items))
        sets.index = len(sets.items) - 1
        return {'FINISHED'}
    
class MOONRAY_OT_RemoveTraceSet(bpy.types.Operator):
    bl_idname = "moonray.remove_trace_set"
    bl_label = "Remove Trace Set"
    bl_description = "Remove the selected trace set from the list"

    def execute(self, context):
        sets = context.scene.moonray.trace_sets
        if sets.items:
            sets.items.remove(sets.index)
            sets.index = min(max(0, sets.index - 1), len(sets.items) - 1)
        return {'FINISHED'}

classes = [MOONRAY_OT_AddLightSet, MOONRAY_OT_RemoveLightSet, MOONRAY_OT_AddLightFilterSet, MOONRAY_OT_RemoveLightFilterSet, MOONRAY_OT_AddShadowSet, MOONRAY_OT_RemoveShadowSet, MOONRAY_OT_AddShadowReceiverSet, MOONRAY_OT_RemoveShadowReceiverSet, MOONRAY_OT_AddTraceSet, MOONRAY_OT_RemoveTraceSet]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)