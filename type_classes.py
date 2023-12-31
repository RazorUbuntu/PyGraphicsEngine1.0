# INFO: STABLE RELEASE v1.0
# This script holds the classes that are used within the Engine.

from error import *

from pygame import display

import numpy as np


# The screen class Handles the properties of a screen.
class Screen3D:
    def __init__(self, label: str, resolution: str):
        # Label of the screen.
        try:
            self.Label = label.title()
        except ValueError:
            show_error_n_exit(TypeOfError.error(f"'Label'", f"'String'"))

        # Fixed Set Resolution of the Screen.
        try:
            self.Resolution = tuple(map(int, resolution.lower().split(sep='x')))

            if len(self.Resolution) != 2:  # Resolution can only have two set numbers.
                show_error_n_exit(UnmatchedArgs.error(f"Resolution of {self.Label} must be of 'Width x Height'", ))
        except ValueError:
            show_error_n_exit(UnmatchedArgs.error(f"Resolution of {self.Label} must be of 'Width x Height'", ))

        # Pygame screen initialization.
        self.Screen = display.set_mode(self.Resolution)

    def __repr__(self):
        return f"{self.Label} Type : Screen where Resolution = {self.Resolution}"


###############################
#         MATH Classes        #
###############################

# A Vector Class, that stores 3-Dimensional spatial points x, y, z.
# Used to define the vertex points of a 3D Model in terms of points.
class Vec3D:
    def __init__(self, coord=(0, 0, 0)):
        # Initialize the points with the 4th 4D point defaulted to 1
        self.x, self.y, self.z = coord[0], coord[1], coord[2]
        self.w = 1

    def __repr__(self):
        # Represent the Vector with its Spatial 3D points, x,y,z and 4D: w (used for Matrix manipulation)
        return f'X = {self.x} : Y = {self.y} : Z = {self.z} : W = {self.w}'

    def __add__(self, other):
        # Adding two Vectors
        vec = Vec3D()
        vec.x, vec.y, vec.z = self.x + other.x, self.y + other.y, self.z + other.z
        return vec

    def __sub__(self, other):
        # Subtracting two Vectors
        vec = Vec3D()
        vec.x, vec.y, vec.z = self.x - other.x, self.y - other.y, self.z - other.z
        return vec

    def __mul__(self, const: float):
        # Vector-Constant Multiplication
        vec = Vec3D()
        vec.x, vec.y, vec.z = self.x * const, self.y * const, self.z * const
        return vec

    def div(self, const: float):
        # Vector-Constant Division
        vec = Vec3D()
        const += 1e-7
        vec.x, vec.y, vec.z = self.x / const, self.y / const, self.z / const
        return vec


# The Triangle class holds 3 Vertex points to form a Face
# Used in modelling 3D meshes.
class Triangle:
    def __init__(self, vec3ds=((0, 0, 0), (0, 0, 0), (0, 0, 0)),
                 lighting: float = None):  # By default, the triangle has zero area

        self.lighting = lighting
        # define a list of 3D points
        self.vectors = []

        # Add the provided 3 points
        for vec in vec3ds:
            
            # if the vector is a Vec3D object then:
            if isinstance(vec, Vec3D):
                vec = (vec.x, vec.y, vec.z)
        
            self.vectors.append(Vec3D(vec))  # Add as Vector Object
        self.total_V = len(self.vectors)  # must always be 3 for a triangle

    def __repr__(self):
        # Represents the Triangle with it's 3 vectors.
        return f'Triangle with vectors:\n{str(self.vectors)}\n'


# The Mesh Class holds the 3D data of triangles to form the Model.
# Used to define Models.

class Mesh:
    def __init__(self, name):  # Initialize the Mesh to start with zero Triangles
        self.triangles = []
        self.name = name

    def __repr__(self):
        return f'MeshCube : {self.name}'

    def __call__(self):
        return self.triangles

    def tris(self, faces_and_vertices):
        faces, vertices = faces_and_vertices
        # Add the Triangles of the 3D Mesh.
        for tri in faces:
            self.triangles.append(Triangle(vertices_trans(tri, vertices)))


def vertices_trans(indexes_list, vertices):
    # Adds Vectors from the VectorFaceData to a temporary list.
    vector_list: list = []
    for idx in indexes_list:
        vector_list.append(vertices[idx-1])

    # returns the formed Triangle
    return vector_list
