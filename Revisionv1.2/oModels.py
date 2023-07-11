from fMesh import *

CubePath = 'C:\\Users\\saadi\\OneDrive\\Documents\\GitHub\\PyGraphics\\PyGraphicsEngine1.0\\Revisionv1.2\\cube.obj'
Cube = Mesh()
Cube.load_objects_from_files(CubePath, 'Cube', start=0)

AxisPath = 'C:\\Users\\saadi\\OneDrive\\Documents\\GitHub\\PyGraphics\\PyGraphicsEngine1.0\\Revisionv1.2\\axis.obj'
Axis = Mesh()
Axis.load_objects_from_files(AxisPath, 'Axis', start=1)