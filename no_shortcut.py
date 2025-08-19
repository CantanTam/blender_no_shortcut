import bpy
from .draw_background import draw_background

def close_gizmo_overlay():
    new_window = bpy.context.window_manager.windows[-1].screen.areas[0].spaces[0]
    new_window.show_gizmo = False
    new_window.overlay.show_overlays = False

class NS_OT_no_shortcut(bpy.types.Operator):
    bl_idname = "wm.no_shortcut"
    bl_label = "快捷键提示"
    bl_description = "快捷键提示"
    bl_options = {'REGISTER', 'UNDO'} 

    def invoke(self, context, event):
        # 新建一个窗口，并关闭新窗口的 gizmo 和 layover
        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')
        bpy.app.timers.register(close_gizmo_overlay, first_interval=0.1)
        bpy.ops.wm.window_fullscreen_toggle()
        bpy.ops.screen.screen_full_area(use_hide_panels=True)
        
        self.handle_backgroud = bpy.types.SpaceView3D.draw_handler_add(draw_background, (self,context), 'WINDOW', 'POST_PIXEL')


        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        if event.type == 'ESC' or event.type == 'ACCENT_GRAVE' and event.alt == True and event.value == 'RELEASE':
            bpy.types.SpaceView3D.draw_handler_remove(self.handle_backgroud, 'WINDOW')
            bpy.ops.wm.window_close()
            return {'FINISHED'}

        if event.type == 'ACCENT_GRAVE':
            return {'RUNNING_MODAL'}

            

        return {'PASS_THROUGH'}
