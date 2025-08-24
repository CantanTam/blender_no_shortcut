import bpy
from .background import draw_background
from .bottom_keys import draw_keys
from . import bottom_keys
from .top_keys import draw_keyboard
from . import top_keys
#from .draw_keys_shader import draw_keys_shader
from . import keys_shader

def close_gizmo_overlay():
    new_window = bpy.context.window_manager.windows[-1].screen.areas[0].spaces[0]
    new_window.show_gizmo = False
    new_window.overlay.show_overlays = False

current_type = None
current_mode = None

class NS_OT_no_shortcut(bpy.types.Operator):
    bl_idname = "wm.no_shortcut"
    bl_label = "快捷键提示"
    bl_description = "快捷键提示"
    bl_options = {'REGISTER', 'UNDO'} 

    @classmethod
    def poll(cls, context):
        return context.active_object

    def invoke(self, context, event):
        global current_type,current_mode

        current_type = context.active_object.type
        current_mode = context.active_object.mode

        bpy.ops.object.mode_set(mode='OBJECT')

        # 新建一个窗口，并关闭新窗口的 gizmo 和 layover
        bpy.ops.screen.area_dupli('INVOKE_DEFAULT')
        bpy.app.timers.register(close_gizmo_overlay, first_interval=0.1)
        bpy.ops.wm.window_fullscreen_toggle()
        bpy.ops.screen.screen_full_area(use_hide_panels=True)
        
        self.handle_backgroud = bpy.types.SpaceView3D.draw_handler_add(draw_background, (self,context), 'WINDOW', 'POST_PIXEL')
        self.handle_key_shader = bpy.types.SpaceView3D.draw_handler_add(keys_shader.draw_keys_shader, (self,context), 'WINDOW', 'POST_PIXEL')
        draw_keyboard("KEYBOARD.png")


        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        typeandmode = bpy.context.active_object.type+bpy.context.active_object.mode
        
        if event.type =='F1':
            draw_keys("F1.png")
            return {'RUNNING_MODAL'}
        
        if event.type == 'F2':
            draw_keys('F2.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'F3':
            draw_keys('F3.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'F4':
            draw_keys('F4.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'F9':
            draw_keys('F9.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'F11':
            draw_keys('F11.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'F12':
            draw_keys('F12.png')
            return {'RUNNING_MODAL'}
        
        if event.type in {'F5','F6','F7','F8','F10'}:
            return {'RUNNING_MODAL'}
        
        if event.type == 'ACCENT_GRAVE':
            draw_keys('`.png')
            if event.ctrl :
                draw_keys('`_CTRL.png')
            if event.shift :
                draw_keys('`_SHIFT.png')
            
            return {'RUNNING_MODAL'}
        
            #and event.alt == True and event.value == 'RELEASE':
            #context.scene.shortcut_mode.mode = not context.scene.shortcut_mode.mode
            #context.scene.update_tag()
            #return {'RUNNING_MODAL'}

        if event.type == 'ONE':
            draw_keys('1.png')
            if event.shift :
                draw_keys('1_SHIFT.png')
            if event.ctrl :
                draw_keys('1_CTRL.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'TWO':
            draw_keys('2.png')
            if event.shift :
                draw_keys('2_SHIFT.png')
            if event.ctrl :
                draw_keys('2_CTRL.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'THREE':
            draw_keys('3.png')
            if event.shift :
                draw_keys('3_SHIFT.png')
            if event.ctrl :
                draw_keys('3_CTRL.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'FOUR':
            draw_keys('4.png')
            if event.shift :
                draw_keys('4_SHIFT.png')
            if event.ctrl :
                draw_keys('4_CTRL.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'FIVE':
            draw_keys('5.png')
            if event.shift :
                draw_keys('5_SHIFT.png')
            if event.ctrl :
                draw_keys('5_CTRL.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'SIX':
            draw_keys('6.png')
            if event.shift :
                draw_keys('6_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'SEVEN':
            draw_keys('7.png')
            if event.shift :
                draw_keys('7_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'EIGHT':
            draw_keys('8.png')
            if event.shift :
                draw_keys('8_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'NINE':
            draw_keys('9.png')
            if event.shift :
                draw_keys('9_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'ZERO':
            draw_keys('0.png')
            if event.shift :
                draw_keys('0_SHIFT.png')
            if event.ctrl :
                draw_keys('0_CTRL.png')
            return {'RUNNING_MODAL'}

        if event.type == 'MINUS':
            draw_keys('MINUS_CTRL.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'EQUAL':
            draw_keys('EQUAL_CTRL.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'TAB':
            draw_keys('TAB.png')
            if event.ctrl :
                draw_keys('TAB_CTRL.png')
            if event.shift :
                draw_keys('TAB_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'Q':
            draw_keys('Q.png')
            if event.ctrl :
                draw_keys('Q_CTRL.png')
            if event.ctrl and event.alt:
                draw_keys('Q_CTRL_ALT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'W':
            draw_keys('W.png')
            if event.alt :
                draw_keys('W_ALT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'E':
            return {'RUNNING_MODAL'}
        
        if event.type == 'R':
            draw_keys('R.png')
            if event.alt :
                draw_keys('R_ALT.png')
            if event.shift :
                draw_keys('R_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'T':
            draw_keys("T.png")
            return {'RUNNING_MODAL'}
        
        if event.type == 'Y':
            return {'RUNNING_MODAL'}
        
        if event.type == 'U':
            return {'RUNNING_MODAL'}
        
        if event.type == 'I':
            draw_keys('I.png')
            if event.alt :
                draw_keys('I_ALT.png')
            if event.ctrl :
                draw_keys('I_CTRL.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'O':
            draw_keys('O.png')
            if event.shift:
                draw_keys('O_SHIFT.png')
            if event.ctrl:
                draw_keys('O_CTRL.png')
            if event.ctrl and event.shift:
                draw_keys('O_CTRL_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'P':
            draw_keys('P.png')
            if event.ctrl:
                draw_keys('P_CTRL.png')
            if event.alt:
                draw_keys('P_ALT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'A':
            draw_keys('A.png')
            if event.alt:
                draw_keys('A_ALT.png')
            if event.ctrl:
                draw_keys('A_CTRL.png')
            if event.shift:
                draw_keys('A_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'S':
            draw_keys('S.png')
            if event.alt:
                draw_keys('S_ALT.png')
            if event.shift:
                draw_keys('S_SHIFT.png')
            if event.ctrl:
                draw_keys('S_CTRL.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'D':
            draw_keys('D.png')
            if event.alt or event.shift:
                draw_keys('D_SHIFT_ALT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'F':
            return {'RUNNING_MODAL'}
        
        if event.type == 'G':
            draw_keys('G.png')
            if event.alt:
                draw_keys('G_ALT.png')
            if event.ctrl:
                draw_keys('G_CTRL.png')
            if event.shift:
                draw_keys('G_SHIFT.png')
            if event.shift and event.alt:
                draw_keys('G_SHIFT_ALT.png')
            if event.ctrl and event.alt:
                draw_keys('G_CTRL_ALT.png')
            if event.ctrl and event.shift:
                draw_keys('G_CTRL_SHIFT.png')
            if event.ctrl and event.shift and event.alt:
                draw_keys('G_CTRL_SHIFT_ALT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'H':
            draw_keys('H.png')
            if event.ctrl:
                draw_keys('H_CTRL.png')
            if event.shift:
                draw_keys('H_SHIFT.png')
            if event.alt:
                draw_keys('H_ALT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'J':
            draw_keys('J.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'K':
            draw_keys('K.png')
            if event.shift:
                draw_keys('K_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'L':
            draw_keys('L.png')
            if event.shift:
                draw_keys('L_SHIFT.png')
            if event.ctrl:
                draw_keys('L_CTRL.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'Z':
            draw_keys('Z.png')
            if event.ctrl:
                draw_keys('Z_CTRL.png')
            if event.shift:
                draw_keys('Z_SHIFT.png')
            if event.alt:
                draw_keys('Z_ALT.png')
            if event.ctrl and event.shift:
                draw_keys('Z_CTRL_SHIFT.png')
            if event.shift and event.alt:
                draw_keys('Z_SHIFT_ALT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'X':
            draw_keys('X.png')
            if event.shift:
                draw_keys('X_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'C':
            draw_keys('C.png')
            if event.ctrl:
                draw_keys('C_CTRL.png')
            if event.shift:
                draw_keys('C_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'V':
            draw_keys('V.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'B':
            draw_keys('B.png')
            if event.shift:
                draw_keys('B_SHIFT.png')
            if event.alt:
                draw_keys('B_ALT.png')
            if event.ctrl or event.ctrl and event.alt:
                draw_keys('B_CTRL_ALT.png')
            if event.ctrl and event.shift:
                draw_keys('B_CTRL_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'N':
            draw_keys('N.png')
            if event.ctrl:
                draw_keys('N_CTRL.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'M':
            draw_keys('M.png')
            if event.ctrl:
                draw_keys('M_CTRL.png')
            if event.shift:
                draw_keys('M_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'COMMA':
            draw_keys('COMMA.png')
            if event.ctrl:
                draw_keys('COMMA_CTRL.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'PERIOD':
            draw_keys('PERIOD.png')
            if event.ctrl:
                draw_keys('PERIOD_CTRL.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'SLASH':
            draw_keys('SLASH.png')
            if event.alt:
                draw_keys('SLASH_ALT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'SPACE':
            draw_keys('SPACE.png')
            if event.ctrl:
                draw_keys('SPACE_CTRL.png')
            if event.shift:
                draw_keys('SPACE_SHIFT.png')
            if event.ctrl and event.shift:
                draw_keys('SPACE_CTRL_SHIFT.png')
            if event.ctrl and event.alt:
                draw_keys('SPACE_CTRL_ALT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'HOME':
            draw_keys('HOME.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'DEL':
            draw_keys('DELETE.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'UP_ARROW':
            draw_keys('UP.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'DOWN_ARROW':
            draw_keys('DOWN.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'LEFT_ARROW':
            draw_keys('LEFT.png')
            if event.shift:
                draw_keys('LEFT_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'RIGHT_ARROW':
            draw_keys('RIGHT.png')
            if event.shift:
                draw_keys('RIGHT_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        

        

        

        
        if event.type == 'CAPSLOCK':
            return {'PASS_THROUGH'}
        
        if event.type == 'ESC':
            bpy.ops.object.mode_set(mode=current_mode)
            bpy.types.SpaceView3D.draw_handler_remove(self.handle_backgroud, 'WINDOW')
            bpy.types.SpaceView3D.draw_handler_remove(self.handle_key_shader, 'WINDOW')

            # 清理残留图片纹理
            if bottom_keys.bottom_key:
                bottom_keys.bottom_key.cleanup()
                bottom_keys.bottom_key = None

            # 清理残留图片纹理
            if top_keys.top_key:
                top_keys.top_key.cleanup()
                top_keys.top_key = None

            if keys_shader.keys_shader_texture:
                # 4.0 以上版本，无需要手动 free()
                if bpy.app.version < (4, 0, 0):
                    keys_shader.keys_shader_texture.free()
                keys_shader.keys_shader_texture = None

            bpy.ops.wm.window_close()
            return {'FINISHED'}
            

        return {'PASS_THROUGH'}
