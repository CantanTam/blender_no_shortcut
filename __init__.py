import bpy
import os
from bpy.app.handlers import persistent


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