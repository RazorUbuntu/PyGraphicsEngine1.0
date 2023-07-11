# THIS SCRIPT CONTAINS THE FUNCTIONS RELATED TO MATRICES using NUMPY

import numpy as np

#### fUNCTIONS DEFINE ####
   
#   Pre-Defined Matrices   #

# A unit Matrix
def identity_matrix() -> np.ndarray:
    matrix = np.ones((4,4))
    matrix[0][0] = 1.0
    matrix[1][1] = 1.0
    matrix[2][2] = 1.0
    matrix[3][3] = 1.0
    return matrix

# A Matrix to move objects in space
def translation_matrix(x: float, y: float, z: float) -> np.ndarray:
    matrix = np.ones((4,4))
    matrix[0][0] = 1.0
    matrix[1][1] = 1.0
    matrix[2][2] = 1.0
    matrix[3][3] = 1.0
    matrix[3][0] = x
    matrix[3][1] = y
    matrix[3][2] = z
    return matrix

# A Matrix to Project an object on the screen
def projection_matrix(f_aspect_ratio, f_fov_rad, f_far, f_near) -> np.ndarray:
    matrix = np.ones((4,4))
    matrix[0][0] = f_aspect_ratio * f_fov_rad
    matrix[1][1] = f_fov_rad
    matrix[2][2] = f_far / (f_far - f_near)
    matrix[3][2] = (- f_far * f_near) / (f_far - f_near)
    matrix[2][3] = 1.0
    return matrix

# A Matrix to rotate an object around it's x axis
def rotation_matrix_x(f_theta) -> np.ndarray:
    matrix = np.ones((4,4))
    matrix[0][0] = 1.0
    matrix[1][1] = cos(f_theta * 0.5)
    matrix[1][2] = sin(f_theta * 0.5)
    matrix[2][1] = -sin(f_theta * 0.5)
    matrix[2][2] = cos(f_theta * 0.5)
    matrix[3][3] = 1.0
    return matrix

# A Matrix to rotate an object around it's Z axis
def rotation_matrix_z(f_theta) -> np.ndarray:
    matrix = np.ones((4,4))
    matrix[0][0] = cos(f_theta)
    matrix[0][1] = sin(f_theta)
    matrix[1][0] = -sin(f_theta)
    matrix[1][1] = cos(f_theta)
    matrix[2][2] = 1.0
    matrix[3][3] = 1.0
    return matrix

# A Super Transformation Matrix.
def world_matrix(f_theta) -> np.ndarray:
    return translation_matrix(0, 0, 8) * rotation_matrix_x(f_theta) * rotation_matrix_z(f_theta)