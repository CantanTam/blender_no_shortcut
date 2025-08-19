import bpy,tkinter,gpu
from gpu_extras.batch import batch_for_shader
from . import width_height

def close_gizmo_overlay():
    new_window = bpy.context.window_manager.windows[-1].screen.areas[0].spaces[0]
    new_window.show_gizmo = False
    new_window.overlay.show_overlays = False

class NS_OT_no_shortcut(bpy.types.Operator):
    bl_idname = "wm.no_shortcut"
    bl_label = "快捷键提示"
    bl_description = "快捷键提示"
    bl_options = {'REGISTER', 'UNDO'} 

    @staticmethod
    def draw_background(self,context):
        vertices = [(0, 0),(width_height.screen_width, 0),(0, width_height.screen_height),(width_height.screen_width, width_height.screen_height)]
        indices = [(0, 1, 2), (2, 1, 3)]
        shader = gpu.shader.from_builtin('UNIFORM_COLOR')
        batch = batch_for_shader(shader, 'TRIS', {"pos": vertices}, indices=indices)

        gpu.state.blend_set('ALPHA')

        shader.bind()
        shader.uniform_float("color",  (0.246, 0.246, 0.246, 1))
        batch.draw(shader)

        gpu.state.blend_set('NONE')

    def invoke(self, context, event):
        # 新建一个窗口，并关闭新窗口的 gizmo 和 layover
        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')
        bpy.app.timers.register(close_gizmo_overlay, first_interval=0.1)
        bpy.ops.wm.window_fullscreen_toggle()
        bpy.ops.screen.screen_full_area(use_hide_panels=True)
        
        self.handle_backgroud = bpy.types.SpaceView3D.draw_handler_add(self.draw_background, (self,context), 'WINDOW', 'POST_PIXEL')


        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        if event.type == 'ESC' or event.type == 'ACCENT_GRAVE' and event.alt == True:
            bpy.types.SpaceView3D.draw_handler_remove(self.handle_backgroud, 'WINDOW')
            bpy.ops.wm.window_close()
            return {'FINISHED'}

        if event.type == 'ACCENT_GRAVE':
            return {'RUNNING_MODAL'}

            

        return {'PASS_THROUGH'}
