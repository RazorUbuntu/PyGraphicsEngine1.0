from settings import *
from pygame import draw
from math import sqrt

class Vec3D:
    def __init__(self, coord = (0,0,0)):
        self.x, self.y, self.z = coord[0], coord[1], coord[2]
        self.w = 1

    def __repr__(self):
        return f'X = {self.x} : Y = {self.y} : Z = {self.z} : W = {self.w}'

    def __add__(self, other):
        vec = Vec3D()
        vec.x, vec.y, vec.z = self.x + other.x, self.y + other.y, self.z + other.z
        return vec

    def __sub__(self, other):
        vec = Vec3D()
        vec.x, vec.y, vec.z = self.x - other.x, self.y - other.y, self.z - other.z
        return vec

    def __mul__(self, const: float):
        vec = Vec3D()
        vec.x, vec.y, vec.z = self.x * const, self.y * const, self.z * const
        return vec

    def div(self, const: float):
        vec = Vec3D()
        const += 1e-7
        vec.x, vec.y, vec.z = self.x / const, self.y / const, self.z / const
        return vec



class Triangle:
    def __init__(self, vec3ds = ((0,0,0),(0,0,0),(0,0,0))):
        self.vectors = []
        for vec in vec3ds:
            self.vectors.append(Vec3D(vec))
        self.total_V = len(self.vectors)

    def __repr__(self):
        return f'Triangle with vectors:\n{str(self.vectors)}\n'
            

class Mesh:
    def __init__(self):
        self.triangles = []

    def tris(self, faces_and_vertices):
        for tri in faces_and_vertices[0]:
            self.triangles.append(Triangle(self.vertice_trans(tri, faces_and_vertices[1])))

    def vertice_trans(self, vertices_list, vertices):
        vector_list = []
        for idx in vertices_list:
            vector_list.append(vertices[idx])
        return vector_list

class SqMatrix:
    def __init__(self, size: int):
        self.size = size
        self.matrix = [[0 for column in range(size)] for row in range(size)]

    def __repr__(self):
        represent = ''
        for row in self.matrix:
            represent += f'{row}\n'
        return represent

    def __mul__(self, other):

        tempMat = SqMatrix(4)

        for row in range(self.size):
            catche = []
            
            add = 0
            for columns in range(other.size):
                
                add = 0
                for index in range(self.size):

                    add += self.matrix[row][index]*other.matrix[index][columns]
                    
                catche.append(add)
                
            tempMat.matrix[row] = catche

        return tempMat
    


###############################
#         FUNCTIONS           #
###############################

def MultiplyMatrixVector(inpVec : Vec3D, Matrix : SqMatrix):

    outVec = Vec3D()

    outVec.x = inpVec.x * Matrix.matrix[0][0] + inpVec.y * Matrix.matrix[1][0] + inpVec.z * Matrix.matrix[2][0] + inpVec.w * Matrix.matrix[3][0]

    outVec.y = inpVec.x * Matrix.matrix[0][1] + inpVec.y * Matrix.matrix[1][1] + inpVec.z * Matrix.matrix[2][1] + inpVec.w * Matrix.matrix[3][1]

    outVec.z = inpVec.x * Matrix.matrix[0][2] + inpVec.y * Matrix.matrix[1][2] + inpVec.z * Matrix.matrix[2][2] + inpVec.w * Matrix.matrix[3][2]

    w: float = inpVec.x * Matrix.matrix[0][3] + inpVec.y * Matrix.matrix[1][3] + inpVec.z * Matrix.matrix[2][3] + inpVec.w * Matrix.matrix[3][3]

    if w != 0.0:
        outVec = outVec.div(w)
    
    return outVec


def FillTriangle(surface, x1 , y1 , x2 , y2 , x3 , y3 , color = 0x2588):

    draw.polygon(surface, color, [(x1, y1), (x2, y2), (x2, y2), (x3, y3), (x3, y3), (x1, y1)])

def DrawTriangle(surface, x1 , y1 , x2 , y2 , x3 , y3 , color = 0x2588, width = 1):

    draw.polygon(surface, color, [(x1, y1), (x2, y2), (x2, y2), (x3, y3), (x3, y3), (x1, y1)], width=width)

def LoadFromObjFile(FilePath, size: float = 1.0):
    vertices = []
    faces = []
    try:
        with open(FilePath, 'r')as ObjFile:
            
            lines = ObjFile.readlines()
            for line in lines:
                
                if line[0] == 'v':
                    temlis = (list(line[2:].split()))
                    vertices.append(tuple(num*size for num in map(float, temlis)))
                    
                elif line[0] == 'f':
                    temlis = (list(line[2:].split()))
                    faces.append(tuple(map(int, temlis)))
                    
        return faces, vertices
    except:pass

###############################
#        VECTOR FUNC          #
###############################

def DotProduct(self, other):
    return self.x * other.x + self.y * other.y + self.z * other.z

def VectorLength(self):
    return sqrt(DotProduct(self, self))

def VectorNormalise(self):
    l: float = VectorLength(self) + 1e-9
    vec = Vec3D()
    vec.x, vec.y, vec.z = self.x / l, self.y / l, self.z / l
    return vec

def CrossProduct(self, other):
    vec = Vec3D()

    vec.x = self.y * other.z - self.z * other.y
    vec.y = self.z * other.x - self.x * other.z
    vec.z = self.x * other.y - self.y * other.x

    return vec

############### PROJECTION MATRIX #################



