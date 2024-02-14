bl_info = {
    "name" : "blender-save-capture",
    "author" : "Airyz",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from bpy.app.handlers import persistent

@persistent
def screenshot_pre_save_handler(dummy):
    if bpy.data.filepath != "":
        bpy.ops.screen.screenshot(filepath=bpy.data.filepath + ".png")

def register():
    bpy.app.handlers.save_pre.append(screenshot_pre_save_handler)

def unregister():
    bpy.app.handlers.save_pre.remove(screenshot_pre_save_handler)