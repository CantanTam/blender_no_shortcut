import bpy

def close_gizmo_overlay():
    current_win = bpy.context.window
    # 找到新窗口
    new_win = None
    for win in bpy.context.window_manager.windows:
        if win != current_win:
            new_win = win
            break

    if new_win:
        for area in new_win.screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.show_gizmo = False
                        space.overlay.show_overlays = False
    return None  # 返回 None 表示不重复调用

class NS_OT_no_shortcut(bpy.types.Operator):
    bl_idname = "wm.no_shortcut"
    bl_label = "快捷键提示"
    bl_description = "快捷键提示"
    bl_options = {'REGISTER', 'UNDO'} 

    def execute(self, context):
        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')

        # 延迟 0.1 秒再关闭新窗口的 gizmo
        bpy.app.timers.register(close_gizmo_overlay, first_interval=0.1)

        bpy.ops.wm.window_fullscreen_toggle()
        bpy.ops.screen.screen_full_area(use_hide_panels=True)

        return {'FINISHED'}
