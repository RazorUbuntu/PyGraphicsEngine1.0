# INFO:
# This script holds the classes that are used within the Engine.

from Errors import *


from os import system
from pygame import display


# The screen class Handles the properties of a screen.
class Screen3D:
    def __init__(self, Label: str, Resolution: str):
        # Label of the screen.
        try:
            self.Label = Label.title()
        except Exception:
            ShowErrorNExit(TypeOfError.Error(f"'Label'", f"'String'"))

        # Fixed Set Resolution of the Screen.
        try:
            self.Resolution = tuple(map(int, Resolution.lower().split(sep='x')))
            
            if len(self.Resolution) != 2: # Resolution can only have two set numbers.
                ShowErrorNExit(UnmatchedArgs.Error(f"Resolution of {self.Label} must be of 'WidthxHeight'",))
        except Exception:
            ShowErrorNExit(UnmatchedArgs.Error(f"Resolution of {self.Label} must be of 'WidthxHeight'",))

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
    
    def __init__(self, coord = (0,0,0)):
        # Initialize the points with the 4th 4D point defaulted to 1
        self.x, self.y, self.z = coord[0], coord[1], coord[2]
        self.w = 1

    def __repr__(self):
        # Represent the Vector with it's Spactial 3D points, x,y,z and 4D: w (used for Matrix manipulation)
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
    def __init__(self, vec3ds = ((0,0,0),(0,0,0),(0,0,0))): # By default the triangle has zero area

        # define a list of 3D points
        self.vectors = []

        # Add the provided 3 points
        for vec in vec3ds:
            self.vectors.append(Vec3D(vec)) # Add as Vector Object
        self.total_V = len(self.vectors) # must always be 3 for a triangle

    def __repr__(self):
        # Represents the Triangle with it's 3 vectors.
        return f'Triangle with vectors:\n{str(self.vectors)}\n'
            
# The Mesh Class holds the 3D data of triangles to form the Model.
# Used to define Models.
class Mesh:
    def __init__(self): # Initialize the Mesh to start with zero Triangles
        self.triangles = []

    def tris(self, faces_and_vertices): 
        # Add the Triangles of the 3D Mesh.
        for tri in faces_and_vertices[0]:
            self.triangles.append(Triangle(self.vertice_trans(tri, faces_and_vertices[1])))

    def vertice_trans(self, vertices_list, vertices):
        # Adds Vectors from the VectorFaceData to a temporary list.
        vector_list = []
        for idx in vertices_list:
            vector_list.append(vertices[idx])

        # returns the formed Triangle
        return vector_list

# Square Matrix Class: Math Concept of an Array of rows and columns.
# Used for making 3D to 2D transformation Matrices, etc.
class SqMatrix:
    def __init__(self, size: int): # initialize the size and a zero matrix,
        self.size = size
        self.matrix = [[0 for column in range(size)] for row in range(size)]

    def __repr__(self):
        # Represents the Matriz rows by row.
        represent = ''
        for row in self.matrix:
            represent += f'{row}\n'
        return represent

    def __mul__(self, other): # Matrix-Matrix Multiplication

        tempMat = SqMatrix(4) # Make an empty temp matrix

        for idx, row in enumerate(self.matrix): # Iterrate through self matrix rows
            catche = [] # Set an Empty row list at the beginning of every iteration
            
            for jdx, columns in enumerate(other.matrix[idx]):# Iterrate through other matrix columns
                
                add = 0 # set to zero at the beginning of every iteration
                for index in range(self.size): #iterate using the size
                    
                    # Matrix calculation:
                    add += self.matrix[idx][index]*other.matrix[index][jdx] 
                    
                catche.append(add) # An Element of the row of the resultant matrix.

            # Set to the new row.    
            tempMat.matrix[row] = catche

        # Return the Resultant matrix from the Matrix Multiplication.
        return tempMat

    def transpose(self):
        for idx, rowlength in enumerate(range(self.size,0,-1)):
            
            for jdx in range(rowlength):
                self.matrix[idx][jdx+idx], self.matrix[jdx+idx][idx] = self.matrix[jdx+idx][idx], self.matrix[idx][jdx+idx]
            
        return self
            
    