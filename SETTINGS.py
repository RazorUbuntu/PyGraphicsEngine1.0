# INFO: STABLE RELEASE v1.0
# Import math
from math import tan

# Game settings
RES = WIDTH, HEIGHT = 720, 720
PIXEL = 4, 4
FPS: int = 500  # Max limit of FPS by pygame is 500 it seems

# Functional settings

f_near = 0.1
f_far = 1000.0
f_fov = 90
f_aspect_ratio = WIDTH / HEIGHT
f_fov_rad = 1.0 / tan(f_fov * 0.5 / 180 * 3.14159)


empty_mat_data = [[0.0 for _ in range(4)] for __ in range(4)]

# Colours:

LIGHT_CONST = 0.00028

colors: dict = {
    'black'         : [0  ,   0,   0],
    'grey'          : [120, 120, 120],
    'white'         : [255, 255, 255],
    'bloody red'    : [60 ,   0,   0],
    'red'           : [255,   0,   0],
    'orange'        : [255, 120,   0],
    'yellow'        : [255, 255,   0],
    'light green'   : [120, 255,   0],
    'dark green'    : [0  ,  60,   0],
    'green'         : [0  , 255,   0],
    'cyan green'    : [0  , 255, 120],
    'cyan'          : [0  , 255, 255],
    'sky blue'      : [0  , 120, 255],
    'blue'          : [0  ,   0, 255],
    'dark blue'     : [0  ,   0,  60],
    'maroon pink'   : [255,   0, 120],
    'pink'          : [255,   0, 255],
    'purple'        : [120,   0, 255]
}
