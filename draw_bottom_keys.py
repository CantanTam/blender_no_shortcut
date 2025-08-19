import bpy,gpu,os
from gpu_extras.batch import batch_for_shader
from . import width_height


class draw_keyss:
    def __init__(self, image_path):
        self.image_path = image_path
        self.handler = None
        self.needs_redraw = False
        self.draw_handler = None

        # 使用固定 notices 文件夹
        if not os.path.isabs(self.image_path):
            script_dir = os.path.dirname(os.path.realpath(__file__))
            script_dir = os.path.normpath(script_dir)
            self.image_path = os.path.normpath(
                os.path.join(script_dir, "shortcuts", self.image_path)
            )

        self.image = bpy.data.images.load(self.image_path)
        self.texture = gpu.texture.from_image(self.image)

        if bpy.app.version <= (4, 0, 0):
            self.shader = gpu.shader.from_builtin('2D_IMAGE')
        else:
            self.shader = gpu.shader.from_builtin('IMAGE')

        self.vertices = {
            "pos": [
                (0, 0),
                (width_height.screen_width, 0),
                (width_height.screen_width, width_height.screen_height),
                (0, width_height.screen_height)
            ],
            "texCoord": [(0, 0), (1, 0), (1, 1), (0, 1)],
        }
        self.batch = batch_for_shader(self.shader, 'TRI_FAN', self.vertices)

        self.draw_handler = bpy.types.SpaceView3D.draw_handler_add(self.view3d_draw_callback, (), 'WINDOW', 'POST_PIXEL')

        bpy.app.timers.register(self.check_redraw, persistent=True)

        self.show()


    def draw(self):
        self.batch = batch_for_shader(self.shader, 'TRI_FAN', self.vertices)
        gpu.state.blend_set('ALPHA')
        self.shader.bind()
        self.shader.uniform_sampler("image", self.texture)
        self.batch.draw(self.shader)
        gpu.state.blend_set('NONE')

    def show(self):
        if self.handler is None:
            self.handler = bpy.types.SpaceView3D.draw_handler_add(
                self.draw, (), 'WINDOW', 'POST_PIXEL'
            )

    def hide(self):
        if self.handler is not None:
            bpy.types.SpaceView3D.draw_handler_remove(self.handler, 'WINDOW')
            self.handler = None

    def view3d_draw_callback(self):
        self.needs_redraw = True

    def check_redraw(self):
        if self.needs_redraw:
            self.hide()
            self.needs_redraw = False
        return 1.0

    def cleanup(self):
        self.hide()
        if self.draw_handler:
            try:
                bpy.types.SpaceView3D.draw_handler_remove(self.draw_handler, 'WINDOW')
            except Exception:
                pass
            self.draw_handler = None

        try:
            bpy.app.timers.unregister(self.check_redraw)
        except Exception:
            pass

        if hasattr(self, 'texture'):
            del self.texture
        if hasattr(self, 'image'):
            del self.image

# 全局控制变量
bottom_key = None

def draw_keys(image_name):
    global bottom_key
    if bottom_key:
        bottom_key.cleanup()
        bottom_key = None
        bpy.app.timers.register(lambda: None, first_interval=0.1)
    
    bottom_key = draw_keyss(image_name)

def register():
    pass

def unregister():
    global bottom_key
    if bottom_key:
        bottom_key.cleanup()
        bottom_key = None
