import bpy
import os

bl_info = {
    "name": "No Shortcut",
    "author": "Canta Tam",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "location": "View3D",
    "description": "让你无需再记快捷键",
    "category": "3D View",
    "doc_url": "https://www.bilibili.com/video/BV12q4y1t7h9/?spm_id_from=333.1387.upload.video_card.click&vd_source=e4cbc5ec88a2d9cfc7450c34eb007abe", 
    "support": "COMMUNITY"
}

ADDON_NAME = os.path.basename(os.path.dirname(__file__))

addon_keymaps = []

from . import width_height	
from .no_shortcut import NS_OT_no_shortcut
from .shortcut_mode import NS_PG_shortcut_mode

def register_keymaps():
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new("wm.no_shortcut", type='ACCENT_GRAVE', value='RELEASE', alt=True)
        addon_keymaps.append((km, kmi))

def unregister_keymaps():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

def register():
    width_height.get_width_height()
    bpy.utils.register_class(NS_OT_no_shortcut)
    bpy.utils.register_class(NS_PG_shortcut_mode)
    bpy.types.Scene.shortcut_mode = bpy.props.PointerProperty(type=NS_PG_shortcut_mode)
    register_keymaps()
    


def unregister():

    unregister_keymaps()
    del bpy.types.Scene.shortcut_mode
    bpy.utils.unregister_class(NS_PG_shortcut_mode)
    bpy.utils.unregister_class(NS_OT_no_shortcut)
    pass
    





if __name__ == "__main__":
    register()