# THIS SCRIPT IS DEDICATED TO VECTORS, THE CLASS, AND RELATED FUNCTIONS

####  IMPORT MODULES  ####

import logging
from ERRORCONSTANTS import *

#### CLASS DEFINITION ####

class Vector3D:

    vec_id = 0

    def __init__(self, coords = (0, 0, 0, 1)):
        
        self.id_num = Vector3D.increment()
        
        if len(coords) == 3:
            self.x, self.y, self.z = coords
            self.alpha = 1
            
        elif len(coords) == 4:
            self.x, self.y, self.z, self.alpha = coords
            
        else:
            self.x, self.y, self.z, self.alpha = (None, None, None, None)


    def __repr__(self) -> str:
        
        if None in (self.x, self.y, self.z, self.alpha):
            return f'Vector <{self.id_num}>: {ERROR.ERROR10001}.'
        
        return f'Vector <{self.id_num}>: with Co-ordinates:\nx = {self.x}; y = {self.y}; z = {self.z}; alpha = {self.alpha}\n\n'


    def __call__(self):
        if None in (self.x, self.y, self.z, self.alpha):
            return (ERROR.ERROR10001, 0, 0, 0)
        return (self.x, self.y, self.z, self.alpha)

    def __add__(self, other):
        # Adding two Vectors
        _vector = Vector3D()
        _vector.x = self.x + other.x
        _vector.y = self.y + other.y
        _vector.z = self.z + other.z
        return _vector


    def __sub__(self, other):
        # Subtracting two Vectors
        _vector = Vector3D()
        _vector.x = self.x - other.x
        _vector.y = self.y - other.y
        _vector.z = self.z - other.z
        return _vector


    def constant_mul(self, const: float):
        # Vector-Constant Multiplication
        _vector = Vector3D()
        _vector.x = self.x * const
        _vector.y = self.y * const
        _vector.z = self.z * const
        return _vector


    def constant_div(self, const: float):
        # Vector-Constant Division
        _vector = Vector3D()
        const += 1e-7
        _vector.x = self.x / const
        _vector.y = self.y / const
        _vector.z = self.z / const
        return _vector

    def rep_as_list(self)-> list:
        return [self.x, self.y, self.z, self.w]
    
    @classmethod
    def increment(cls):
        cls.vec_id += 1
        return cls.vec_id


#### fUNCTIONS DEFINE ####

def dot_product(_vector_a, _vector_b) -> float:
    return _vector_a.x * _vector_b.x + _vector_a.y * _vector_b.y + _vector_a.z * _vector_b.z


def vector_length(_vector_a) -> float:
    return sqrt(dot_product(_vector_a, _vector_a))


def vector_normalise(_vector_a) -> Vector3D:
    l: float = vector_length(_vector_a) + 1e-9
    _vector = Vec3D()
    _vector.x = _vector_a.x / l
    _vector.y = _vector_a.y / l
    _vector.z = _vector_a.z / l
    return _vector


def cross_product(_vector_a, _vector_b) -> Vector3D:
    _vector = Vec3D()

    _vector.x = _vector_a.y * _vector_b.z - _vector_a.z * _vector_b.y
    _vector.y = _vector_a.z * _vector_b.x - _vector_a.x * _vector_b.z
    _vector.z = _vector_a.x * _vector_b.y - _vector_a.y * _vector_b.x

    return _vector