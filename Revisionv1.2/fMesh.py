# THIS SCRIPT IS DEDICATED TO TRIANGLES, THE CLASS, AND RELATED FUNCTIONS

####  IMPORT MODULES  ####

from fTriangles import * # Also imports fVectors, logging and ERRORCONSTANTS | clear_screen

#### CLASS DEFINITION ####

class Mesh():

    mesh_id = 0

    def __init__(self, name: str = None, seq_of_triangles: list = ()) -> None:
        self.triangles = seq_of_triangles
        self.name = name
        self.mesh_id = Mesh.increment()

    def load_objects_from_files(self, file_path, name: str = None, size: float = 1.0, start: int = 1) -> None:
        
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
                    vector_list.append(Vector3D(vertices[idx - start]))
                    
                self.triangles.append(Triangle(vector_list))

        # exception for if file-not-found comes up.
        except FileNotFoundError:
            system('cls')
            logging.error(f'The File at {file_path} does not exist or is not of .obj data type!')

    def __repr__(self) -> str:
        return ''.join(['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n',
                        f'[Mesh: {self.name}] with [ID: {self.mesh_id}]: with Triangles:\n',
                        'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n',
                        f'{self.triangles}\n',
                        '---------------------------------------------------------------------------------------------------\n'])

    def represent(self, _range: int = 1) -> None:
        result: list = ['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                        f'[Mesh: {self.name}] with [ID: {self.mesh_id}]: with Triangles:',
                        'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n',]
        
        for triangle in self.triangles[:_range]:
            result.append(triangle)
        

        result += ['-------------------------------------------------------------------------',
                   f'{len(self.triangles) - _range * 2} Triangles in between {self.triangles[_range - 1].tri_id} to {self.triangles[-_range].tri_id}',
                   '-------------------------------------------------------------------------\n']
        
        for triangle in self.triangles[-_range:]:
            result.append(triangle)

        result.append('---------------------------------------------------------------------------------------------------')

        for line in result: print(line)
        
        
    @classmethod
    def increment(cls) -> None:
        
        cls.mesh_id += 1
        return cls.mesh_id
