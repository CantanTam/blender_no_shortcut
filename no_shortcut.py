import bpy

shortcut_window = False

def close_gizmo_overlay():
    new_window = bpy.context.window_manager.windows[-1].screen.areas[0].spaces[0]
    new_window.show_gizmo = False
    new_window.overlay.show_overlays = False

class NS_OT_no_shortcut(bpy.types.Operator):
    bl_idname = "wm.no_shortcut"
    bl_label = "快捷键提示"
    bl_description = "快捷键提示"
    bl_options = {'REGISTER', 'UNDO'} 

    def execute(self, context):
        global shortcut_window

        if not shortcut_window:
            bpy.ops.screen.area_dupli('INVOKE_DEFAULT')

            # 延迟 0.1 秒再关闭新窗口的 gizmo
            bpy.app.timers.register(close_gizmo_overlay, first_interval=0.1)

            bpy.ops.wm.window_fullscreen_toggle()
            bpy.ops.screen.screen_full_area(use_hide_panels=True)

            shortcut_window = True

        else:
            bpy.ops.wm.window_close()
            shortcut_window = False

        return {'FINISHED'}
