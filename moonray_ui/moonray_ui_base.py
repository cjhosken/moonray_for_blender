import bpy

class _MoonRayPanelHeader():
    COMPAT_ENGINES = {"MOONRAY"}

    @classmethod
    def poll(cls, context):
        return context.engine in cls.COMPAT_ENGINES

class MOONRAY_UL_Basic_UIList(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.prop(item, 'name', text='', emboss=False, icon_value=icon)   

class CollectionPanel(_MoonRayPanelHeader):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'

    def _draw_collection(self, context, layout, ptr, name, operator,
                         opcontext, prop_coll, collection_index, default_name='', ui_list_class="MOONRAY_UL_Basic_UIList", enable_add_func=None, enable_remove_func=None):
        layout.label(text=name)
        row = layout.row()
        row.template_list(ui_list_class, "PRMAN", ptr, prop_coll, ptr,
                          collection_index, rows=1)
        col = row.column(align=True)

        row = col.row()
        if enable_add_func:
            row.enabled = enable_add_func(context)
        if operator != '':
            op = row.operator(operator, icon="ADD", text="")
            op.context = opcontext
            op.collection = prop_coll
            op.collection_index = collection_index
            op.defaultname = default_name
            op.action = 'ADD'

            row = col.row()
            if enable_remove_func:
                row.enabled = enable_remove_func(context)
            op = row.operator(operator, icon="REMOVE", text="")
            op.context = opcontext
            op.collection = prop_coll
            op.collection_index = collection_index
            op.action = 'REMOVE'

        if hasattr(ptr, prop_coll) and len(getattr(ptr, prop_coll)) > 0 and \
                getattr(ptr, collection_index) >= 0:
            idx = getattr(ptr, collection_index)
            coll = getattr(ptr, prop_coll)
            if idx >= len(coll):
                return
            item = coll[idx]
            self.draw_item(layout, context, item)

class MoonRayButtonsPanel(_MoonRayPanelHeader):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.render.engine == "MOONRAY"
    

class ShaderNodePanel(_MoonRayPanelHeader):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_label = 'Node Panel'

    bl_context = ""

    @classmethod
    def poll(cls, context):
        if not _MoonRayPanelHeader.poll(context):
            return False
        if cls.bl_context == 'material':
            if context.material and context.material.node_tree != '':
                return True
        if cls.bl_context == 'data':
            if not context.light:
                return False
            if context.light.moonray.use_moonray_node:
                return True
        return False

class ShaderPanel(_MoonRayPanelHeader):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'

    shader_type = 'surface'
    param_exclude = {}

    @classmethod
    def poll(cls, context):
        is_moonray = _MoonRayPanelHeader.poll(context)
        if cls.bl_context == 'data' and cls.shader_type == 'light':
            return (hasattr(context, "light") and context.light is not None and is_moonray)
        elif cls.bl_context == 'world':
            return (hasattr(context, "world") and context.world is not None and is_moonray)
        elif cls.bl_context == 'material':
            return (hasattr(context, "material") and context.material is not None and is_moonray)
        

classes = [
    MOONRAY_UL_Basic_UIList
]