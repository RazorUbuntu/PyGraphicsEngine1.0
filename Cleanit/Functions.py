# This script will have hold of all the functions defined for usage in all around the project
# except for Error Handling.

from type_classes import *


##########################
#    MATRIX FUNCTIONS    #
##########################

# It multiplies a Vector with a matrix.
def MultiplyMatrixVector(inpVec : Vec3D, Matrix : SqMatrix):

    '''
    outVec = Vec3D()

    outVec.x = inpVec.x * Matrix.matrix[0][0] + inpVec.y * Matrix.matrix[1][0] + inpVec.z * Matrix.matrix[2][0] + inpVec.w * Matrix.matrix[3][0]

    outVec.y = inpVec.x * Matrix.matrix[0][1] + inpVec.y * Matrix.matrix[1][1] + inpVec.z * Matrix.matrix[2][1] + inpVec.w * Matrix.matrix[3][1]

    outVec.z = inpVec.x * Matrix.matrix[0][2] + inpVec.y * Matrix.matrix[1][2] + inpVec.z * Matrix.matrix[2][2] + inpVec.w * Matrix.matrix[3][2]

    w: float = inpVec.x * Matrix.matrix[0][3] + inpVec.y * Matrix.matrix[1][3] + inpVec.z * Matrix.matrix[2][3] + inpVec.w * Matrix.matrix[3][3]
    '''

    OutCatche = [0,0,0,0]
    VCatche = inpVec.x , inpVec.y, inpVec.z, inpVec.w
    print(VCatche)
    MCatche = Matrix.transpose().matrix
    print(MCatche)

    for idx, row in enumerate(MCatche):
        sum_overall = 0
        for jdx, element in enumerate(row):
            sum_overall += VCatche[jdx] * element
        OutCatche[idx] = sum_overall

    outVec = Vec3D(OutCatche)
    
    if outVec.w != 0.0:
        outVec = outVec.div(outVec.w)
    
    return outVec

