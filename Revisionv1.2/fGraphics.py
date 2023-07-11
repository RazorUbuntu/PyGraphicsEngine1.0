# THIS SCRIPT IS DEDICATED TO GRAPHIC RELATED FUNCTIONS

from fVectors import *
from pygame import draw

#### fUNCTIONS DEFINE ####

# This function creates a filled 3 sided polygon with set color.
def fill_triangle(surface, triangle: Triangle, color=0x2588) -> None:
    x1 = triangle.vectors[0].x
    y1 = triangle.vectors[0].y

    x2 = triangle.vectors[1].x
    y2 = triangle.vectors[1].y

    x3 = triangle.vectors[2].x
    y3 = triangle.vectors[2].y

    draw.polygon(surface, color, [(x1, y1), (x2, y2), (x2, y2),
                                  (x3, y3), (x3, y3), (x1, y1)])


# This function creates a hollow 3 sided polygon with set color and set width.
def draw_triangle(surface, triangle: Triangle, color=0x2588, width=1) -> None:
    x1 = triangle.vectors[0].x
    y1 = triangle.vectors[0].y

    x2 = triangle.vectors[1].x
    y2 = triangle.vectors[1].y

    x3 = triangle.vectors[2].x
    y3 = triangle.vectors[2].y

    draw.polygon(surface, color, [(x1, y1), (x2, y2), (x2, y2),
                                  (x3, y3), (x3, y3), (x1, y1)], width=width)
