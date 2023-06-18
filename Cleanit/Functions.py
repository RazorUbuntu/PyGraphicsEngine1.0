# This script will have hold of all the functions defined for usage in all around the project
# except for Error Handling.

from type_classes import Vec3D, Triangle, Mesh, SqMatrix

from math import sin, cos, tan, sqrt
from pygame import draw
from os import system
import logging


# Sums one list's elements with the other.
def sum_in_list(l1, l2):
    if len(l1) >= len(l2):
        for idx, item in enumerate(l2):
            l1[idx] += item
        return l1

    else:
        for idx, item in enumerate(l1):
            l2[idx] += item
        return l2


##########################
#    MATRIX FUNCTIONS    #
##########################

# It multiplies a Vector with a matrix.
def multiply_matrix_vector(inp_vector: Vec3D, matrix: SqMatrix):
    temp_cache, out_cache = [0, 0, 0, 0], [0, 0, 0, 0]
    v_cache = inp_vector.x, inp_vector.y, inp_vector.z, inp_vector.w
    m_cache = matrix.matrix

    for idx, v_item in enumerate(v_cache):  # [0, 1, 2, 3], item
        temp_cache = [0, 0, 0, 0]
        for jdx in range(matrix.size):  # [0, 1, 2, 3: index]
            temp_cache[jdx] = v_cache[idx] * m_cache[idx][jdx]
        out_cache = sum_in_list(out_cache, temp_cache)

    out_vector = Vec3D(out_cache)

    if out_vector.w != 0.0:
        out_vector = out_vector.div(out_vector.w)

    return out_vector


#   Pre-Defined Matrices   #

def identity_matrix(matrix):
    matrix.matrix[0][0] = 1.0
    matrix.matrix[1][1] = 1.0
    matrix.matrix[2][2] = 1.0
    matrix.matrix[3][3] = 1.0
    return matrix


def translation_matrix(matrix, x: float, y: float, z: float):
    matrix.matrix[0][0] = 1.0
    matrix.matrix[1][1] = 1.0
    matrix.matrix[2][2] = 1.0
    matrix.matrix[3][3] = 1.0
    matrix.matrix[3][0] = x
    matrix.matrix[3][1] = y
    matrix.matrix[3][2] = z
    return matrix


def projection_matrix(matrix, f_aspect_ratio, f_fov_rad, f_fov, f_far, f_near):
    matrix.matrix[0][0] = f_aspect_ratio * f_fov_rad
    matrix.matrix[1][1] = f_fov_rad
    matrix.matrix[2][2] = f_far / (f_far - f_near)
    matrix.matrix[3][2] = (- f_far * f_near) / (f_far - f_near)
    matrix.matrix[2][3] = 1.0
    return matrix


def rotation_matrix_z(matrix, f_theta):
    matrix.matrix[0][0] = cos(f_theta)
    matrix.matrix[0][1] = sin(f_theta)
    matrix.matrix[1][0] = -sin(f_theta)
    matrix.matrix[1][1] = cos(f_theta)
    matrix.matrix[2][2] = 1.0
    matrix.matrix[3][3] = 1.0
    return matrix


def rotation_matrix_x(matrix, f_theta):
    matrix.matrix[0][0] = 1.0
    matrix.matrix[1][1] = cos(f_theta * 0.5)
    matrix.matrix[1][2] = sin(f_theta * 0.5)
    matrix.matrix[2][1] = -sin(f_theta * 0.5)
    matrix.matrix[2][2] = cos(f_theta * 0.5)
    matrix.matrix[3][3] = 1.0
    return matrix


###############################
#      VECTOR FUNCTIONS       #
###############################

def dot_product(self, other):
    return self.x * other.x + self.y * other.y + self.z * other.z


def vector_length(self):
    return sqrt(dot_product(self, self))


def vector_normalise(self):
    l: float = vector_length(self) + 1e-9
    vec = Vec3D()
    vec.x, vec.y, vec.z = self.x / l, self.y / l, self.z / l
    return vec


def cross_product(self, other):
    vec = Vec3D()

    vec.x = self.y * other.z - self.z * other.y
    vec.y = self.z * other.x - self.x * other.z
    vec.z = self.x * other.y - self.y * other.x

    return vec


###############################
#     GRAPHIC FUNCTIONS       #
###############################

# This function creates a filled 3 sided polygon with set color.
def fill_triangle(surface, x1, y1, x2, y2, x3, y3, color=0x2588):
    draw.polygon(surface, color, [(x1, y1), (x2, y2), (x2, y2),
                                  (x3, y3), (x3, y3), (x1, y1)])


# This function creates a hollow 3 sided polygon with set color and set width.
def draw_triangle(surface, x1, y1, x2, y2, x3, y3, color=0x2588, width=1):
    draw.polygon(surface, color, [(x1, y1), (x2, y2), (x2, y2),
                                  (x3, y3), (x3, y3), (x1, y1)], width=width)


# This function loads a model into a mesh format from an object file. <.obj>
def load_from_obj_file(file_path, size: float = 1.0):

    # set some empty lists.
    vertices = []
    faces = []
    try:  # exception for if file-not-found comes up.
        with open(file_path, 'r') as ObjFile:
            lines = ObjFile.readlines()  # store the lines in a variable.

            for line in lines:  # iterate through each line to determine whether one is face or a vertex.

                if line[0] == 'v':  # if v is the starting character it is a vertex.
                    temlis = (list(line[2:].split()))
                    vertices.append(tuple(num * size for num in map(float, temlis)))

                elif line[0] == 'f':  # if f is the starting character it is a face.
                    temlis = (list(line[2:].split()))
                    faces.append(tuple(map(int, temlis)))

        # if there is no face or vertex, the file may be formatted different or is invalid.
        if faces == [] or vertices == []:
            system('cls')
            logging.error(f'The File at {file_path} does not exist or is not of .obj data type!')

        # Return the mesh data.
        return faces, vertices

    # exception for if file-not-found comes up.
    except FileNotFoundError:
        system('cls')
        logging.error(f'The File at {file_path} does not exist or is not of .obj data type!')
