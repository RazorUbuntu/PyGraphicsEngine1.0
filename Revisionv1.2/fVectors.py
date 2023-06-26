# THIS SCRIPT IS DEDICATED TO VECTORS, THE CLASS, AND RELATED FUNCTIONS

####  IMPORT MODULES  ####

import logging
from ERRORCONSTANTS import *

#### CLASS DEFINITION ####

vec_id_num: int = 0
class Vector3D:

    def __init__(self, coords = (0, 0, 0, 1)):
        
        global vec_id_num
        self.id_num = vec_id_num
        
        if len(coords) == 3:
            self.x, self.y, self.z = coords
            self.alpha = 1
            
        elif len(coords) == 4:
            self.x, self.y, self.z, self.alpha = coords
            
        else:
            self.x, self.y, self.z, self.alpha = (None, None, None, None)
        vec_id_num += 1


    def __repr__(self) -> str:
        
        if None in (self.x, self.y, self.z, self.alpha):
            return f'Vector {self.id_num}: {ERROR.ERROR10001}.'
        
        return f'Vector {self.id_num}: with Co-ordinates:\nx = {self.x}; y = {self.y}; z = {self.z}; alpha = {self.alpha}\n\n'


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


#### fUNCTIONS DEFINE ####
