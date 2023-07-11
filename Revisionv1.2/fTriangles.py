# THIS SCRIPT IS DEDICATED TO TRIANGLES, THE CLASS, AND RELATED FUNCTIONS

####  IMPORT MODULES  ####

import logging
import ERRORCONSTANTS
from fVectors import *
from SETTINGS import clear_screen as CS
CS()

#### CLASS DEFINITION ####

class Triangle():

    tri_id = 0
    
    def __init__(self, seq_of_vectors: list) -> None:
        
        if isinstance(seq_of_vectors[0], Vector3D):
            self.vectors = seq_of_vectors
        else:
            self.vectors = self.convert_seq_to_vectors(seq_of_vectors)
            
        self.tri_id = Triangle.increment()


    def __repr__(self) -> str:
        
        if len(self.vectors) > 3:
            return f'Polygon [{self.tri_id}] with Vectors:\n\n{self.vectors}'
        return f'Triangle [{self.tri_id}] with Vectors:\n\n{self.vectors}'

    def shift(shift_vector : Vector3D) -> None:
        for idx, vector in enumrate(self.vectors):
            self.vectors[idx] = vector + shift_vector

    def convert_seq_to_vectors(self, seq_of_vectors) -> list:
        
        # tuple -> vector
        local_temp = []
        
        for vector in seq_of_vectors:
            local_temp.append(Vector3D(vector))
            
        return local_temp


    @classmethod
    def increment(cls) -> int:
        
        cls.tri_id += 1
        return cls.tri_id