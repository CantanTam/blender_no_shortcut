import bpy,gpu,os
from gpu_extras.batch import batch_for_shader
from . import width_height

keys_shader_texture= None

def get_keys_shader():
    global keys_shader_texture
    script_dir = os.path.normpath(os.path.dirname(os.path.realpath(__file__)))
    image_name = "SHADER.png"

    image_path = os.path.normpath(os.path.join(script_dir, "shortcuts", image_name))

    # 加载图片（避免重复加载）
    if image_name not in bpy.data.images:
        image = bpy.data.images.load(image_path)
    else:
        image = bpy.data.images[image_name]

    # 转换成 GPU 纹理
    keys_shader_texture= gpu.texture.from_image(image)
    return keys_shader_texture



def draw_keys_shader(self,context):
    if bpy.app.version <= (4, 0, 0):
        shader = gpu.shader.from_builtin('2D_IMAGE')
    else:
        shader = gpu.shader.from_builtin('IMAGE')

    vertices = {
        "pos": [
            (0, 0),
            (width_height.screen_width, 0),
            (width_height.screen_width, width_height.screen_height),
            (0, width_height.screen_height)
        ],
        "texCoord": [(0, 0), (1, 0), (1, 1), (0, 1)],
    }

    batch = batch_for_shader(shader, 'TRI_FAN', vertices)
    gpu.state.blend_set('ALPHA')
    shader.bind()
    shader.uniform_sampler("image", get_keys_shader())
    batch.draw(shader)
    gpu.state.blend_set('NONE')





