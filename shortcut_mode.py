import bpy

class NS_PG_shortcut_mode(bpy.types.PropertyGroup):
    mode: bpy.props.BoolProperty(
        name="显示模式",
        description="按照键盘模式显示或者按照功能模式显示",
        default=False
    )