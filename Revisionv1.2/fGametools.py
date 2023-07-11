from fNumPy import *
from fTriangles import *

def Transform(triangle: Triangle, shift_vector : Vector3D, *args) -> Triangle:
    # Args are the function transformations to make to the triangle
    __triangle__: list = []

    # Triangle's vectors are shifter by a set value.
    triangle.shift(shift_vector)

    # The transform is a 4x4 Matrix that is multiplied with the vectors of the triangle.
    for transform in args:
        
        for idx, vector in enumerate(triangle):
            # Multiply using dot method.
            __triangle__ += [Vector3D(transform.dot(vector.rep_as_list()))]

    return __triangle__

def Sorting(triangles: list) -> list:
    
    return sorted(triangles, key=lambda _triangle: lambda_sort_triangles(_triangle))

