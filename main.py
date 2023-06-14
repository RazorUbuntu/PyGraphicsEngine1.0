import pygame as pg
import sys
from settings import *
from classesXFuncs import *
from time import time
from math import sqrt

class GameEngine:
    def __init__(self):
        pg.init()
        self.start_time = time()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()

    def new_game(self):
        pass

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')
        self.current_time = time() - self.start_time

    def draw(self):
        self.screen.fill('black')
        list_of_tri = []

        # DRAW TRIS
        for tri in meshCube.triangles:
            
            triProjected, triTranslated = Triangle(), Triangle()
            triRotatedZ, triRotatedZX = Triangle(), Triangle()

            for i in range(tri.total_V):
                triRotatedZ.vectors[i] = MultiplyMatrixVector(tri.vectors[i], mat_rot_z)
                triRotatedZX.vectors[i] = MultiplyMatrixVector(triRotatedZ.vectors[i], mat_rot_x)


            # shift from origin
            for i in range(tri.total_V):
                triTranslated.vectors[i].x = triRotatedZX.vectors[i].x - 0.0
                triTranslated.vectors[i].y = triRotatedZX.vectors[i].y - 0.0
                triTranslated.vectors[i].z = triRotatedZX.vectors[i].z + 3.0

            normal, line1, line2 = Vec3D(), Vec3D(), Vec3D()

            line1.x = triTranslated.vectors[1].x - triTranslated.vectors[0].x
            line1.y = triTranslated.vectors[1].y - triTranslated.vectors[0].y
            line1.z = triTranslated.vectors[1].z - triTranslated.vectors[0].z

            line2.x = triTranslated.vectors[2].x - triTranslated.vectors[0].x
            line2.y = triTranslated.vectors[2].y - triTranslated.vectors[0].y
            line2.z = triTranslated.vectors[2].z - triTranslated.vectors[0].z

            normal.x = line1.y * line2.z - line1.z * line2.y
            normal.y = line1.z * line2.x - line1.x * line2.z
            normal.z = line1.x * line2.y - line1.y * line2.x

            len_norm = sqrt(normal.x**2 + normal.y**2 + normal.z**2) + 5e-7

            normal.x /= len_norm; normal.y /= len_norm; normal.z /= len_norm
            
            if  normal.z < 0: pass

            if (normal.x * (triTranslated.vectors[0].x - vCamera.x) + 
                normal.y * (triTranslated.vectors[0].y - vCamera.y) +
                normal.z * (triTranslated.vectors[0].z - vCamera.z) < 0):

                light_direction = Vec3D((0.0, 0.0, -1.0))

                len_light_direction = sqrt(light_direction.x**2 + light_direction.y**2 + light_direction.z**2) + 5e-7

                light_direction.x /= len_light_direction
                light_direction.y /= len_light_direction
                light_direction.z /= len_light_direction

                light_dp = normal.x * light_direction.x + normal.y * light_direction.y + normal.z * light_direction.z

                # Transform 3d to 2d
                for i in range(tri.total_V):
                    triProjected.vectors[i] = MultiplyMatrixVector(triTranslated.vectors[i], mat_proj)
                    # SCALE TO VIEW
                    triProjected.vectors[i].x += 1.0
                    triProjected.vectors[i].y += 1.0

                    triProjected.vectors[i].x *= 0.5 * WIDTH
                    triProjected.vectors[i].y *= 0.5 * WIDTH       

                FillTriangle(self.screen, triProjected.vectors[0].x,
                            triProjected.vectors[0].y, triProjected.vectors[1].x, triProjected.vectors[1].y,
                            triProjected.vectors[2].x, triProjected.vectors[2].y,
                            color=(25.5 * light_dp * 10, 1 * light_dp * 10, 25.5 * light_dp * 10))        
                
                # DrawTriangle(self.screen, triProjected.vectors[0].x,
                #             triProjected.vectors[0].y, triProjected.vectors[1].x, triProjected.vectors[1].y,
                #             triProjected.vectors[2].x, triProjected.vectors[2].y,
                #             color=(0,0,0),
                #             width = 3)
                
                # Store the triangles for sorting.
                list_of_tri.append(triProjected)



        # Rasterize Triangles       

        for triProjected in list_of_tri: pass
            
            
            
            
            

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.type == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        global fTheta, mat_rot_x, mat_rot_z
        
        while True:
            self.check_event()
            self.update()
            self.draw()
            
            fTheta = self.current_time
            mat_rot_x = RotationMatrix_X(mat_rot_x, fTheta)
            mat_rot_z = RotationMatrix_Z(mat_rot_z, fTheta)


if __name__ == '__main__':
    
    GE = GameEngine()
    #! ON-USER-CREATE {
         
    ################################
    #      CLASS DECLARATION:      #
    ################################
    
    meshCube = Mesh()
    mat_proj = SqMatrix(4)
    mat_rot_z = SqMatrix(4)
    mat_rot_x = SqMatrix(4)
    ident = SqMatrix(4)
       
    ################################
    #      DEFINED VARIABLES:      #
    ################################
    
    mat_proj = ProjectionMatrix(mat_proj, fAspectRatio, fFovRad, fFov, fFar, fNear)
    vCamera = Vec3D()
    meshCube.tris(LoadFromObjFile('cube.obj', 1.0))
    
    ################################

    #! }
    GE.run()

