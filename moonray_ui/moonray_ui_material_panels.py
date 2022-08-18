import bpy
from .moonray_ui_base import MoonRayPanel


class MATERIAL_PT_moonray_preview(MoonRayPanel, bpy.types.Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "material"
    bl_label = "Preview"

    @classmethod
    def poll(cls, context):
        if not MoonRayPanel.poll(context):
            return False   

        mat = getattr(context, 'material', None)
        
        if not mat:
            return False 
        return True      

    def draw(self, context):
        layout = self.layout
        mat = context.material
        row = layout.row()

        if mat:
            row.template_preview(context.material, show_buttons=1)

class MATERIAL_PT_moonray_shader_surface(MoonRayPanel, bpy.types.Panel):
    bl_context = "material"
    bl_label = "MoonRay Surface"
    shader_type = 'Shader'

    def draw(self, context):
        layout = self.layout

class MOONRAY_PT_context_material(MoonRayPanel, bpy.types.Panel):
    bl_context = "material"
    bl_options = {'HIDE_HEADER'}

    @classmethod
    def poll(cls, context):
        ob = context.active_object

        if ob and ob.type == "GPENCIL":
            return False
        else:
            return (context.material or context.object) and MoonRayPanel.poll(context)

    def draw(self, context):
        layout = self.layout

        mat = context.material
        ob = context.object
        slot = context.material_slot
        space = context.space_data

        if ob:
            is_sortable = len(ob.material_slots) > 1
            rows = 3
            if (is_sortable):
                rows = 4

            row = layout.row()

            row.template_list("MATERIAL_UL_matslots", "", ob, "material_slots", ob, "active_material_index", rows=rows)

            col = row.column(align=True)
            col.operator("object.material_slot_add", icon='ADD', text="")
            col.operator("object.material_slot_remove", icon='REMOVE', text="")
            col.separator()
            col.menu("MATERIAL_MT_context_menu", icon='DOWNARROW_HLT', text="")

            if is_sortable:
                col.separator()

                col.operator("object.material_slot_move", icon='TRIA_UP', text="").direction = 'UP'
                col.operator("object.material_slot_move", icon='TRIA_DOWN', text="").direction = 'DOWN'

            if ob.mode == 'EDIT':
                row = layout.row(align=True)
                row.operator("object.material_slot_assign", text="Assign")
                row.operator("object.material_slot_select", text="Select")
                row.operator("object.material_slot_deselect", text="Deselect")

        row = layout.row()

        if ob:
            row.template_ID(ob, "active_material", new="material.new")

            if slot:
                icon_link = "MESH_DATA" if slot.link == "DATA" else "OBJECT_DATA"
                row.prop(slot, "link", text="", icon=icon_link, icon_only=True)

        elif mat:
            layout.template_ID(space, "pin_id")
            layout.separator()

classes = [MATERIAL_PT_moonray_preview, MATERIAL_PT_moonray_shader_surface ,MOONRAY_PT_context_material]