# Import math
from math import sin, cos, tan

# Game settings
RES = WIDTH, HEIGHT = 720, 720
PIXEL = 4, 4
FPS: int = 144

# Functional settings

f_near = 0.1
f_far = 1000.0
f_fov = 90
f_aspect_ratio = WIDTH / HEIGHT
f_fov_rad = 1.0 / tan(f_fov * 0.5 / 180 * 3.14159)
