# THIS SCRIPT IS DEDICATED TO TRIANGLES, THE CLASS, AND RELATED FUNCTIONS

####  IMPORT MODULES  ####

import logging
import ERRORCONSTANTS
from fVectors import *
from fTriangles import *
from os import system
#### CLASS DEFINITION ####


class Mesh():

    def __init__(self, name: str = None, seq_of_triangles: list = ()):
        self.triangles = seq_of_triangles
        self.name = name

    def load_objects_from_files(self, file_path, name: str = None, size: float = 1.0):
        
        # set some empty lists.
        self.name = name
        self.triangles = []
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

            # Add the Triangles of the 3D Mesh.
            for triangle in faces:
                vector_list = []
                
                for idx in triangle:
                    vector_list.append(Vector3D(vertices[idx]))
                    
                self.triangles.append(Triangle(vector_list))

        # exception for if file-not-found comes up.
        except FileNotFoundError:
            system('cls')
            logging.error(f'The File at {file_path} does not exist or is not of .obj data type!')

    def __repr__(self):
        return f'Mesh {self.name}: with Triangles:\n((({self.triangles})))'

Cube = Mesh()
Cube.load_objects_from_files('C:\\Users\\saadi\\OneDrive\\Documents\\GitHub\\PyGraphics\\PyGraphicsEngine1.0\\Revisionv1.2\\cube.obj', 'Cube')
print(Cube)