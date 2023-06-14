# Import math
from math import sin, cos, tan
from time import time

# Game settings
RES = WIDTH, HEIGHT = 720,720
PIXEL = 4,4
FPS = 144

# Functional settings

fTheta = 0
fNear  = 0.1
fFar = 1000.0
fFov = 90
fAspectRatio = WIDTH/HEIGHT
fFovRad = 1.0 / tan(fFov * 0.5 / 180 * 3.14159)

# Matrices

def IdentityMatrix(MATRIX):
    MATRIX.matrix[0][0] = 1.0
    MATRIX.matrix[1][1] = 1.0
    MATRIX.matrix[2][2] = 1.0
    MATRIX.matrix[3][3] = 1.0
    return MATRIX

def TranslationMatrix(MATRIX, x:float, y: float, z: float):
    MATRIX.matrix[0][0] = 1.0
    MATRIX.matrix[1][1] = 1.0
    MATRIX.matrix[2][2] = 1.0
    MATRIX.matrix[3][3] = 1.0
    MATRIX.matrix[3][0] = x
    MATRIX.matrix[3][1] = y
    MATRIX.matrix[3][2] = z
    return MATRIX

def ProjectionMatrix(MATRIX, fAspectRatio, fFovRad, fFov, fFar, fNear):
    MATRIX.matrix[0][0] = fAspectRatio * fFovRad
    MATRIX.matrix[1][1] = fFovRad
    MATRIX.matrix[2][2] = fFar / (fFar - fNear)
    MATRIX.matrix[3][2] = (- fFar * fNear) / (fFar - fNear)
    MATRIX.matrix[2][3] = 1.0
    return MATRIX

def RotationMatrix_Z(MATRIX, fTheta):
    MATRIX.matrix[0][0] = cos(fTheta)
    MATRIX.matrix[0][1] = sin(fTheta)
    MATRIX.matrix[1][0] = -sin(fTheta)
    MATRIX.matrix[1][1] = cos(fTheta)
    MATRIX.matrix[2][2] = 1.0
    MATRIX.matrix[3][3] = 1.0
    return MATRIX

def RotationMatrix_X(MATRIX, fTheta):
    MATRIX.matrix[0][0] = 1.0
    MATRIX.matrix[1][1] = cos(fTheta * 0.5)
    MATRIX.matrix[1][2] = sin(fTheta * 0.5)
    MATRIX.matrix[2][1] = -sin(fTheta * 0.5)
    MATRIX.matrix[2][2] = cos(fTheta * 0.5)
    MATRIX.matrix[3][3] = 1.0
    return MATRIX