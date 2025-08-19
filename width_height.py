import bpy
import tkinter

screen_width = None
screen_width = None

def get_width_height():
    global screen_width,screen_height

    # 通过 tkinter 获取当前屏幕的宽、高
    screen = tkinter.Tk()
    screen.withdraw()
    screen_width = screen.winfo_screenwidth()
    screen_height = screen.winfo_screenheight()
    screen.destroy()