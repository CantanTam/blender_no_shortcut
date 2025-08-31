import bpy
from .background import draw_background
from .bottom_keys import draw_keys
from . import bottom_keys
#from .top_keys import draw_keyboard
from . import top_keys
#from .draw_keys_shader import draw_keys_shader
from . import keys_shader

def close_gizmo_overlay():
    new_window = bpy.context.window_manager.windows[-1].screen.areas[0].spaces[0]
    new_window.show_gizmo = False
    new_window.overlay.show_overlays = False

current_type = None
current_mode = None

context_mode = None

class NS_OT_no_shortcut(bpy.types.Operator):
    bl_idname = "wm.no_shortcut"
    bl_label = "快捷键提示"
    bl_description = "快捷键提示"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object and context.mode in {'OBJECT','EDIT_MESH'}

    def invoke(self, context, event):
        global current_type,current_mode,context_mode

        context_mode = context.mode
        bottom_keys.bottom_context_mode = context.mode

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
        #draw_keyboard("KEYBOARD_OBJECT.png")
        draw_keys('TEST.png')


        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
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
            draw_keys('ACCENT_GRAVE.png')
            if event.ctrl :
                draw_keys('ACCENT_GRAVE_CTRL.png')
            if event.shift :
                draw_keys('ACCENT_GRAVE_SHIFT.png')
            
            return {'RUNNING_MODAL'}
        
            #and event.alt == True and event.value == 'RELEASE':
            #context.scene.shortcut_mode.mode = not context.scene.shortcut_mode.mode
            #context.scene.update_tag()
            #return {'RUNNING_MODAL'}

        if event.type == 'ONE':
            if context_mode == 'OBJECT':
                draw_keys('1.png')
                if event.shift :
                    draw_keys('1_SHIFT.png')
                if event.ctrl :
                    draw_keys('1_CTRL.png')
            elif context_mode == 'EDIT_MESH':
                draw_keys('1_2_3_EDIT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'TWO':
            if context_mode == 'OBJECT':
                draw_keys('2.png')
                if event.shift :
                    draw_keys('2_SHIFT.png')
                if event.ctrl :
                    draw_keys('2_CTRL.png')
            elif context_mode == 'EDIT_MESH':
                draw_keys('1_2_3_EDIT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'THREE':
            if context_mode == 'OBJECT':
                draw_keys('3.png')
                if event.shift :
                    draw_keys('3_SHIFT.png')
                if event.ctrl :
                    draw_keys('3_CTRL.png')
            elif context_mode == 'EDIT_MESH':
                draw_keys('1_2_3_EDIT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'FOUR':
            if context_mode == 'OBJECT':
                draw_keys('4.png')
                if event.shift :
                    draw_keys('4_SHIFT.png')
                if event.ctrl :
                    draw_keys('4_CTRL.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'FIVE':
            if context_mode == 'OBJECT':
                draw_keys('5.png')
                if event.shift :
                    draw_keys('5_SHIFT.png')
                if event.ctrl :
                    draw_keys('5_CTRL.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'SIX':
            if context_mode == 'OBJECT':
                draw_keys('6.png')
                if event.shift :
                    draw_keys('6_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'SEVEN':
            if context_mode == 'OBJECT':
                draw_keys('7.png')
                if event.shift :
                    draw_keys('7_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'EIGHT':
            if context_mode == 'OBJECT':
                draw_keys('8.png')
                if event.shift :
                    draw_keys('8_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'NINE':
            if context_mode == 'OBJECT':
                draw_keys('9.png')
                if event.shift :
                    draw_keys('9_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'ZERO':
            if context_mode == 'OBJECT':
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
            if event.ctrl and event.shift:
                draw_keys('TAB_CTRL_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'LEFT_BRACKET':
            if context_mode == 'OBJECT':
                draw_keys('LEFT_BRACKET_AND_RIGHT_BRACKET.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'RIGHT_BRACKET':
            if context_mode == 'OBJECT':
                draw_keys('LEFT_BRACKET_AND_RIGHT_BRACKET.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'Q':
            if context_mode == 'OBJECT':
                draw_keys('Q.png')
                if event.ctrl :
                    draw_keys('Q_CTRL.png')
                if event.ctrl and event.alt:
                    draw_keys('Q_CTRL_ALT.png')

            if context_mode == 'EDIT_MESH':
                draw_keys('Q_EDIT.png')
                if event.ctrl :
                    draw_keys('Q_CTRL_EDIT.png')
                if event.alt:
                    draw_keys('Q_ALT_EDIT.png')
                if event.ctrl and event.alt:
                    draw_keys('Q_CTRL_ALT_EDIT.png')
                
            return {'RUNNING_MODAL'}
        
        if event.type == 'W':
            if context_mode == 'OBJECT':
                draw_keys('W.png')
                if event.alt :
                    draw_keys('W_ALT.png')

            if context_mode == 'EDIT_MESH':
                draw_keys('W_EDIT.png')
                if event.alt :
                    draw_keys('W_ALT_EDIT.png')
                if event.shift:
                    draw_keys('W_SHIFT_EDIT.png')
                
            return {'RUNNING_MODAL'}
        
        if event.type == 'E':
            if context_mode == 'EDIT_MESH':
                draw_keys('E_EDIT.png')
                if event.ctrl:
                    draw_keys('E_CTRL_EDIT.png')
                if event.shift:
                    draw_keys('E_SHIFT_EDIT.png')
                if event.alt:
                    draw_keys('E_ALT_EDIT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'R':
            if context_mode == 'OBJECT':
                draw_keys('R.png')
                if event.alt :
                    draw_keys('R_ALT.png')
                if event.shift :
                    draw_keys('R_SHIFT.png')

            if context_mode == 'EDIT_MESH':
                draw_keys('R_EDIT.png')
                if event.ctrl:
                    draw_keys('R_CTRL_EDIT.png')
                if event.shift:
                    draw_keys('R_SHIFT_EDIT.png')
                if event.ctrl and event.shift:
                    draw_keys('R_CTRL_SHIFT_EDIT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'T':
            if context_mode == 'OBJECT':
                draw_keys("T.png")
                if event.shift:
                    draw_keys('T_SHIFT.png')
            if context_mode == 'EDIT_MESH':
                draw_keys('T_EDIT.png')
                if event.ctrl or event.shift:
                    draw_keys('T_CTRL_SHIFT_EDIT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'Y':
            if context_mode == 'EDIT_MESH':
                draw_keys('Y_EDIT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'U':
            if context_mode == 'EDIT_MESH':
                draw_keys('U_EDIT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'I':
            if context_mode == 'OBJECT':
                draw_keys('I.png')
                if event.alt :
                    draw_keys('I_ALT.png')
                if event.ctrl :
                    draw_keys('I_CTRL.png')

            if context_mode == 'EDIT_MESH':
                draw_keys('I_EDIT.png')
                if event.ctrl:
                    draw_keys('I_CTRL_EDIT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'O':
            if context_mode == 'OBJECT':
                draw_keys('O.png')
                if event.shift:
                    draw_keys('O_SHIFT.png')
                if event.ctrl:
                    draw_keys('O_CTRL.png')
                if event.ctrl and event.shift:
                    draw_keys('O_CTRL_SHIFT.png')
            
            if context_mode == 'EDIT_MESH':
                draw_keys('O_EDIT.png')
                if event.shift:
                    draw_keys('O_SHIFT.png')
                if event.ctrl:
                    draw_keys('O_CTRL.png')
                if event.ctrl and event.shift:
                    draw_keys('O_CTRL_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'P':
            if context_mode == 'OBJECT':
                draw_keys('P.png')
                if event.ctrl:
                    draw_keys('P_CTRL.png')
                if event.alt:
                    draw_keys('P_ALT.png')

            if context_mode == 'EDIT_MESH':
                draw_keys('P_EDIT.png')
                if event.ctrl:
                    draw_keys('P_CTRL_EDIT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'A':
            if context_mode == 'OBJECT':
                draw_keys('A.png')
                if event.alt:
                    draw_keys('A_ALT.png')
                if event.ctrl:
                    draw_keys('A_CTRL.png')
                if event.shift:
                    draw_keys('A_SHIFT.png')

            if context_mode == 'EDIT_MESH':
                draw_keys('A_EDIT.png')
                if event.ctrl:
                    draw_keys('A_CTRL_EDIT.png')
                if event.shift:
                    draw_keys('A_SHIFT_EDIT.png')
                if event.alt:
                    draw_keys('A_ALT_EDIT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'S':
            if context_mode == 'OBJECT':
                draw_keys('S.png')
                if event.alt:
                    draw_keys('S_ALT.png')
                if event.shift:
                    draw_keys('S_SHIFT.png')
                if event.ctrl:
                    draw_keys('S_CTRL.png')

            if context_mode == 'EDIT_MESH':
                draw_keys('S_EDIT.png')
                if event.ctrl:
                    draw_keys('S_CTRL_EDIT.png')
                if event.shift:
                    draw_keys('S_SHIFT_EDIT.png')
                if event.alt:
                    draw_keys('S_ALT_EDIT.png')
                if event.shift and event.alt:
                    draw_keys('S_SHIFT_ALT_EDIT.png')
                if event.ctrl and event.shift and event.alt:
                    draw_keys('S_CTRL_SHIFT_ALT_EDIT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'D':
            if context_mode == 'OBJECT':
                draw_keys('D.png')
                if event.alt or event.shift:
                    draw_keys('D_SHIFT_AND_ALT.png')
            if context_mode == 'EDIT_MESH':
                draw_keys('D_EDIT.png')
                if event.shift:
                    draw_keys('D_SHIFT_EDIT.png')
                if event.alt:
                    draw_keys('D_ALT_EDIT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'F':
            if context_mode == 'EDIT_MESH':
                draw_keys('F_EDIT.png')
                if event.ctrl:
                    draw_keys('F_CTRL_EDIT.png')
                if event.alt:
                    draw_keys('F_ALT_EDIT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'G':
            if context_mode == 'OBJECT':
                draw_keys('G.png')
                if event.ctrl:
                    draw_keys('G_CTRL.png')
                if event.shift:
                    draw_keys('G_SHIFT.png')
                if event.alt:
                    draw_keys('G_ALT.png')
                if event.ctrl and event.shift:
                    draw_keys('G_CTRL_SHIFT.png')
                if event.ctrl and event.alt:
                    draw_keys('G_CTRL_ALT.png')
                if event.shift and event.alt:
                    draw_keys('G_SHIFT_ALT.png')
                if event.ctrl and event.shift and event.alt:
                    draw_keys('G_CTRL_SHIFT_ALT.png')

            if context_mode == 'EDIT_MESH':
                draw_keys('G_EDIT.png')
                if event.shift:
                    draw_keys('G_SHIFT_EDIT.png')
                if event.ctrl:
                    draw_keys('G_CTRL_EDIT.png')
                if event.ctrl and event.alt:
                    draw_keys('G_CTRL_ALT_EDIT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'H':
            if context_mode == 'OBJECT':
                draw_keys('H.png')
                if event.ctrl:
                    draw_keys('H_CTRL.png')
                if event.shift:
                    draw_keys('H_SHIFT.png')
                if event.alt:
                    draw_keys('H_ALT.png')

            if context_mode == 'EDIT_MESH':
                draw_keys('H_EDIT.png')
                if event.ctrl:
                    draw_keys('H_CTRL_EDIT.png')
                if event.shift:
                    draw_keys('H_SHIFT_EDIT.png')
                if event.alt:
                    draw_keys('H_ALT_EDIT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'J':
            if context_mode == 'OBJECT':
                draw_keys('J.png')
            
            if context_mode == 'EDIT_MESH':
                draw_keys('J_EDIT.png')
                if event.alt:
                    draw_keys('J_ALT_EDIT.png')

            return {'RUNNING_MODAL'}
            
        
        if event.type == 'K':
            if context_mode == 'OBJECT':
                draw_keys('K.png')
                if event.shift:
                    draw_keys('K_SHIFT.png')
            
            if context_mode == 'EDIT_MESH':
                draw_keys('K_EDIT.png')
                if event.shift:
                    draw_keys('K_SHIFT_EDIT.png')

            return {'RUNNING_MODAL'}
        
        if event.type == 'L':
            if context_mode == 'OBJECT':
                draw_keys('L.png')
                if event.shift:
                    draw_keys('L_SHIFT.png')
                if event.ctrl:
                    draw_keys('L_CTRL.png')

            if context_mode == 'EDIT_MESH':
                draw_keys('L_EDIT.png')
                if event.ctrl:
                    draw_keys('L_CTRL_EDIT.png')
                if event.shift:
                    draw_keys('L_SHIFT_EDIT.png')
                if event.alt:
                    draw_keys('L_ALT_EDIT.png')
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
            if context_mode == 'OBJECT':
                draw_keys('X.png')
                if event.shift:
                    draw_keys('X_SHIFT.png')

            if context_mode == 'EDIT_MESH':
                draw_keys('X_EDIT.png')
                if event.ctrl:
                    draw_keys('X_CTRL_EDIT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'C':
            if context_mode == 'OBJECT':
                draw_keys('C.png')
                if event.ctrl:
                    draw_keys('C_CTRL.png')
                if event.shift:
                    draw_keys('C_SHIFT.png')

            if context_mode == 'EDIT_MESH':
                draw_keys('C_EDIT.png')
                if event.ctrl:
                    draw_keys('C_CTRL_EDIT.png')
                if event.shift:
                    draw_keys('C_SHIFT_EDIT.png')
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
            if context_mode == 'OBJECT':
                draw_keys('DELETE.png')

            if context_mode == 'EDIT_MESH':
                draw_keys('DELETE_EDIT.png')
                if event.ctrl:
                    draw_keys('DELETE_CTRL_EDIT.png')

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
        
        if event.type == 'NUMPAD_SLASH':
            draw_keys('NUM_SLASH.png')
            if event.alt:
                draw_keys('NUM_SLASH_ALT.png')
            if event.ctrl or event.shift:
                draw_keys('NUM_SLASH_CTRL_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'NUMPAD_ASTERIX':
            draw_keys('NUM_ASTERIX.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'NUMPAD_MINUS':
            draw_keys('NUM_MINUS.png')
            if event.ctrl or event.shift:
                draw_keys('NUM_MINUS_CTRL_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'NUMPAD_PLUS':
            draw_keys('NUM_PLUS.png')
            if event.ctrl or event.shift:
                draw_keys('NUM_PLUS_CTRL_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'NUMPAD_7':
            draw_keys('NUM_7.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'NUMPAD_1':
            draw_keys('NUM_1.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'NUMPAD_3':
            draw_keys('NUM_3.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'NUMPAD_9':
            draw_keys('NUM_9.png')
            return {'RUNNING_MODAL'}

        if event.type == 'NUMPAD_5':
            draw_keys('NUM_5.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'NUMPAD_4':
            draw_keys('NUM_4.png')
            if event.ctrl:
                draw_keys('NUM_4_CTRL.png')
            if event.shift:
                draw_keys('NUM_4_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'NUMPAD_6':
            draw_keys('NUM_6.png')
            if event.ctrl:
                draw_keys('NUM_6_CTRL.png')
            if event.shift:
                draw_keys('NUM_6_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'NUMPAD_8':
            draw_keys('NUM_8.png')
            if event.ctrl:
                draw_keys('NUM_8_CTRL.png')
            return {'RUNNING_MODAL'}

        if event.type == 'NUMPAD_2':
            draw_keys('NUM_2.png')
            if event.ctrl:
                draw_keys('NUM_2_CTRL.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'NUMPAD_0':
            draw_keys('NUM_0.png')
            if event.ctrl:
                draw_keys('NUM_0_CTRL.png')
            if event.ctrl and event.alt:
                draw_keys('NUM_0_CTRL_ALT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'NUMPAD_PERIOD':
            draw_keys('NUM_PERIOD.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'MIDDLEMOUSE':
            bottom_keys.mouse_click = True
            draw_keys('MOUSE_MIDDLE.png')
            if event.ctrl:
                bottom_keys.mouse_click = True
                draw_keys('MOUSE_MIDDLE_CTRL.png')
            if event.shift:
                bottom_keys.mouse_click = True
                draw_keys('MOUSE_MIDDLE_SHIFT.png')
            if event.alt:
                bottom_keys.mouse_click = True
                draw_keys('MOUSE_MIDDLE_ALT.png')
            if event.ctrl and event.shift:
                bottom_keys.mouse_click = True
                draw_keys('MOUSE_MIDDLE_CTRL_SHIFT.png')
            return {'RUNNING_MODAL'}

        if event.type in {'WHEELUPMOUSE','WHEELDOWNMOUSE'}:
            bottom_keys.mouse_click = True
            draw_keys('MOUSE_MIDDLE_UP_DOWN.png')
            if event.alt:
                bottom_keys.mouse_click = True
                draw_keys('MOUSE_MIDDLE_UP_DOWN_ALT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'LEFTMOUSE':
            bottom_keys.mouse_click = True
            draw_keys('MOUSE_LEFT.png')
            return {'RUNNING_MODAL'}
        
        if event.type == 'RIGHTMOUSE':
            bottom_keys.mouse_click = True
            draw_keys('MOUSE_RIGHT.png')
            if event.ctrl:
                bottom_keys.mouse_click = True
                draw_keys('MOUSE_RIGHT_CTRL.png')
            if event.shift:
                bottom_keys.mouse_click = True
                draw_keys('MOUSE_RIGHT_SHIFT.png')
            return {'RUNNING_MODAL'}
        
        # 鼠标移动直接 回到 modal
        if event.type == 'MOUSEMOVE':
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
