# INFO: STABLE RELEASE v1.0
# This script will have hold of all the functions defined for usage in all around the project
# except for Error Handling.

from type_classes import Vec3D, Triangle

from math import sin, cos, sqrt
from pygame import draw
from os import system
import numpy as np
import logging
from SETTINGS import *


# Sums one list's elements with the other.
def sum_in_list(l1, l2) -> list:
    if len(l1) >= len(l2):
        for idx, item in enumerate(l2):
            l1[idx] += item
        return l1

    else:
        for idx, item in enumerate(l1):
            l2[idx] += item
        return l2


# Multiplies a sequence's elements with a constant.
def mul_seq_const2tup(seq, const) -> tuple:  # 0 -> 255
    list_ = list(seq)

    for idx, element in enumerate(list_):
        if element * const < 0:
            list_[idx] = 0
        elif element * const >= 255:
            list_[idx] = 255
        else:
            list_[idx] = element * const


    return tuple(list_)


##########################
#    MATRIX FUNCTIONS    #
##########################

# It multiplies a Vector with a matrix.
def multiply_matrix_vector(inp_vector: Vec3D, matrix) -> Vec3D:
    temp_cache, out_cache = [0, 0, 0, 0], [0, 0, 0, 0]
    v_cache = inp_vector.x, inp_vector.y, inp_vector.z, inp_vector.w
    m_cache = matrix.matrix

    for idx, v_item in enumerate(v_cache):  # [0, 1, 2, 3], item
        temp_cache = [0, 0, 0, 0]
        for jdx in range(matrix.size):  # [0, 1, 2, 3: index]
            temp_cache[jdx] = v_cache[idx] * m_cache[idx][jdx]
        out_cache = sum_in_list(out_cache, temp_cache)

    out_vector = Vec3D(out_cache)

    return out_vector


def multiply_matrix_vector_factory(inp_vec: Vec3D, matrix: np.ndarray) -> Vec3D:
    out_vec = Vec3D()

    out_vec.x = inp_vec.x * matrix[0][0] + inp_vec.y * matrix[1][0] + inp_vec.z * matrix[2][0] + inp_vec.w * matrix[3][0]

    out_vec.y = inp_vec.x * matrix[0][1] + inp_vec.y * matrix[1][1] + inp_vec.z * matrix[2][1] + inp_vec.w * matrix[3][1]

    out_vec.z = inp_vec.x * matrix[0][2] + inp_vec.y * matrix[1][2] + inp_vec.z * matrix[2][2] + inp_vec.w * matrix[3][2]

    out_vec.w = inp_vec.x * matrix[0][3] + inp_vec.y * matrix[1][3] + inp_vec.z * matrix[2][3] + inp_vec.w * matrix[3][3]

    return out_vec


#   Pre-Defined Matrices   #
def identity_matrix() -> np.ndarray:
    matrix = np.array(empty_mat_data)
    matrix[0][0] = 1.0
    matrix[1][1] = 1.0
    matrix[2][2] = 1.0
    matrix[3][3] = 1.0
    return matrix


def translation_matrix(x: float, y: float, z: float):
    matrix = np.array(empty_mat_data)
    matrix[0][0] = 1.0
    matrix[1][1] = 1.0
    matrix[2][2] = 1.0
    matrix[3][3] = 1.0
    matrix[3][0] = x
    matrix[3][1] = y
    matrix[3][2] = z
    return matrix


def projection_matrix(_f_aspect_ratio, _f_fov_rad, _f_far, _f_near):
    matrix = np.array(empty_mat_data)
    matrix[0][0] = _f_aspect_ratio * _f_fov_rad
    matrix[1][1] = _f_fov_rad
    matrix[2][2] = _f_far / (_f_far - _f_near)
    matrix[3][2] = (- _f_far * _f_near) / (_f_far - _f_near)
    matrix[2][3] = 1.0
    return matrix


def rotation_matrix_z(f_theta):
    matrix = np.array(empty_mat_data)
    matrix[0][0] = cos(f_theta)
    matrix[0][1] = sin(f_theta)
    matrix[1][0] = -sin(f_theta)
    matrix[1][1] = cos(f_theta)
    matrix[2][2] = 1.0
    matrix[3][3] = 1.0
    return matrix


def rotation_matrix_x(f_theta):
    matrix = np.array(empty_mat_data)
    matrix[0][0] = 1.0
    matrix[1][1] = cos(f_theta * 0.5)
    matrix[1][2] = sin(f_theta * 0.5)
    matrix[2][1] = -sin(f_theta * 0.5)
    matrix[2][2] = cos(f_theta * 0.5)
    matrix[3][3] = 1.0
    return matrix


###############################
#      VECTOR FUNCTIONS       #
###############################

def dot_product(vector_a, vector_b) -> float:
    return vector_a.x * vector_b.x + vector_a.y * vector_b.y + vector_a.z * vector_b.z


def vector_length(vector_a) -> float:
    return sqrt(dot_product(vector_a, vector_a))


def vector_normalise(vector_a) -> Vec3D:
    l: float = vector_length(vector_a) + 1e-9
    vec = Vec3D()
    vec.x, vec.y, vec.z = vector_a.x / l, vector_a.y / l, vector_a.z / l
    return vec


def cross_product(vector_a, vector_b) -> Vec3D:
    vec = Vec3D()

    vec.x = vector_a.y * vector_b.z - vector_a.z * vector_b.y
    vec.y = vector_a.z * vector_b.x - vector_a.x * vector_b.z
    vec.z = vector_a.x * vector_b.y - vector_a.y * vector_b.x

    return vec


###############################
#     GRAPHIC FUNCTIONS       #
###############################

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


# This function loads a model into a mesh format from an object file. <.obj>
def load_from_obj_file(file_path, size: float = 1.0) -> tuple:
    # set some empty lists.
    vertices = []
    faces = []
    try:  # exception for if file-not-found comes up.
        with open(file_path, 'r') as ObjFile:
            lines = ObjFile.readlines()  # store the lines in a variable.

            for line in lines:  # iterate through each line to determine whether one is face or a vertex.

                if line[0] == 'v':  # if v is the starting character it is a vertex.
                    temp_list = (list(line[2:].split()))
                    vertices.append(tuple(num * size for num in map(float, temp_list)))

                elif line[0] == 'f':  # if f is the starting character it is a face.
                    temp_list = (list(line[2:].split()))
                    faces.append(tuple(map(int, temp_list)))

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


def conv_to_tuple(vector_list: list) -> tuple:
    temp = []
    for vector in vector_list:
        temp.append((vector.x, vector.y, vector.z))
    return tuple(temp)