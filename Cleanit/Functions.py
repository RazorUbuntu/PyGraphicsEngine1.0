# This script will have hold of all the functions defined for usage in all around the project
# except for Error Handling.

from type_classes import *


##########################
#    MATRIX FUNCTIONS    #
##########################

# It multiplies a Vector with a matrix.
def multiply_matrix_vector(inp_vector: Vec3D, matrix: SqMatrix):

    # outVec = Vec3D()
    #
    # outVec.x = inpVec.x * Matrix.matrix[0][0] + inpVec.y * Matrix.matrix[1][0] + inpVec.z * Matrix.matrix[2][0] + inpVec.w * Matrix.matrix[3][0]
    #
    # outVec.y = inpVec.x * Matrix.matrix[0][1] + inpVec.y * Matrix.matrix[1][1] + inpVec.z * Matrix.matrix[2][1] + inpVec.w * Matrix.matrix[3][1]
    #
    # outVec.z = inpVec.x * Matrix.matrix[0][2] + inpVec.y * Matrix.matrix[1][2] + inpVec.z * Matrix.matrix[2][2] + inpVec.w * Matrix.matrix[3][2]
    #
    # w: float = inpVec.x * Matrix.matrix[0][3] + inpVec.y * Matrix.matrix[1][3] + inpVec.z * Matrix.matrix[2][3] + inpVec.w * Matrix.matrix[3][3]

    out_cache = [0, 0, 0, 0]
    v_cache = inp_vector.x, inp_vector.y, inp_vector.z, inp_vector.w
    print(v_cache)
    m_cache = matrix.transpose().matrix
    print(m_cache)

    for idx, row in enumerate(m_cache):
        sum_overall = 0
        for jdx, element in enumerate(row):
            sum_overall += v_cache[jdx] * element
        out_cache[idx] = sum_overall

    out_vector = Vec3D(out_cache)
    
    if out_vector.w != 0.0:
        out_vector = out_vector.div(out_vector.w)
    
    return out_vector

