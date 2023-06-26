# THIS SCRIPT IS DEDICATED TO TRIANGLES, THE CLASS, AND RELATED FUNCTIONS

####  IMPORT MODULES  ####

import logging
import ERRORCONSTANTS
from fVectors import *

#### CLASS DEFINITION ####

class Triangle():

    def __init__(self, seq_of_vectors: list):
        if isinstance(seq_of_vectors[0], Vector3D):
            self.vectors = seq_of_vectors
        else:
            self.vectors = self.convert_seq_to_vectors(seq_of_vectors)

    def __repr__(self) -> str:
        if len(self.vectors) > 3:
            return f'Polygon with Vectors:\n{self.vectors}'
        return f'Triangle with Vectors:\n{self.vectors}'

    def convert_seq_to_vectors(self, seq_of_vectors):
        # tuple -> vector
        local_temp = []
        for vector in seq_of_vectors:
            local_temp.append(Vector3D(vector))
        return local_temp
