from fNumPy import *
from fTriangles import * # Also imports fVectors, logging and ERRORCONSTANTS | clear_screen
from pygame import draw

def Transform(triangle: Triangle, shift_vector : Vector3D, *args) -> Triangle:
    # Args are the function transformations to make to the triangle
    __triangle__: list = []

    # Triangle's vectors are shifter by a set value.
    triangle.shift(shift_vector)

    # The transform is a 4x4 Matrix that is multiplied with the vectors of the triangle.
    for transform in args:
        
        for vector in triangle:
            # Multiply using dot method.
            __triangle__ += [Vector3D(transform.dot(vector.rep_as_list()))]

    return __triangle__

def Sorting(triangles: list) -> list:
    return sorted(triangles, key=lambda __triangle__:   \
        -(__triangle__.vectors[0].z                     \
            + __triangle__.vectors[1].z                 \
                + __triangle__.vectors[2].z) / 3.0)

def Lighting(triangle: Triangle) -> Triangle:
    pass

def Projection(triangle: Triangle) -> Triangle:
    __triangle__: list = []
    
    for vector in triangle:
        # Multiply using dot method.
        __triangle__ += [Vector3D(transform.dot(vector.rep_as_list()))]
        
    return __triangle__
        

# This function creates a 3 sided polygon with set color and set width.
def Draw(surface, triangle: Triangle, color = 0x2588, width:int = 0) -> None:
    x1 = triangle.vectors[0].x
    y1 = triangle.vectors[0].y

    x2 = triangle.vectors[1].x
    y2 = triangle.vectors[1].y

    x3 = triangle.vectors[2].x
    y3 = triangle.vectors[2].y

    # if Width is set to 0, then the shape is filled else hollow.
    draw.polygon(surface, color, [(x1, y1), (x2, y2), (x2, y2),
                                  (x3, y3), (x3, y3), (x1, y1)], width=width)
    