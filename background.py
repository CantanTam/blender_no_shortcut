import gpu
from gpu_extras.batch import batch_for_shader
from . import width_height

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