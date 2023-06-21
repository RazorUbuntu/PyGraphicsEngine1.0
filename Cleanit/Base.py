# INFO:
# This is the base script that runs the screen and the given objects, physics, scripts etc.


###############################
#         Self Imports        #
###############################

from type_classes import *
from Functions import *
from Errors import *
from SETTINGS import *

###############################
#           Imports           #
###############################

import pygame as pg
import sys
from time import time
from math import sqrt


###############################
#            Begin            #
###############################

def check_event():  # Check for User Input / an Event
    # Event loop
    for event in pg.event.get():

        # Exit the Engine if either escape or the quit button is pressed.
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.type == pg.K_ESCAPE):
            # End the PyGame instance
            pg.quit()

            # Exit the interpreter
            sys.exit()


def draw_triangles(surface, triangles):
    for triangle in triangles:
        fill_triangle(surface, triangle, color='white')
        draw_triangle(surface, triangle, color='black', width=2.0)


class Game3DEngine:  # The main class to start the Engine

    def __init__(self):  # Initialize the minimum requirements

        # PRIVATE VARIABLES: FIXED

        self.mat_prjct: SqMatrix = projection_matrix(f_aspect_ratio, f_fov_rad, f_fov, f_far, f_near)
        self.mat_trans: SqMatrix = translation_matrix(x=0.0, y=0.0, z=3.0)
        self.mat_ident: SqMatrix = identity_matrix()

        self.vt_camera: Vec3D    = Vec3D()

        self.f_theta  : float    = 0.0
        self.mat_rot_z: SqMatrix = SqMatrix(4)
        self.mat_rot_x: SqMatrix = SqMatrix(4)

        # Pygame init func
        pg.init()

        # Deploy the Screen: TODO: Use Screen3D class
        self.screen = pg.display.set_mode(RES)

        # An object to help keep track of time
        self.clock = pg.time.Clock()
        self.init_time = time()
        self.current_time = None

    def update(self):  # Update the screen every call

        # Update the entire screen
        pg.display.flip()

        # Update the screen to this number of Frames-Per-Second
        self.clock.tick(FPS)

        # Show FPS next to the Icon
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')
        self.current_time = self.init_time - time()

        # Changing angle value as the cube rotates.
        self.f_theta = self.current_time

        # Updating the rotational matrices with the new theta value.
        self.mat_rot_z = rotation_matrix_z(self.f_theta)
        self.mat_rot_x = rotation_matrix_x(self.f_theta)

    def draw(self):  # not working
        # clear the screen
        self.screen.fill('black')
        triangles: list = []

        # for triangle in mesh_cube:
        #     tri_rot_z = self.rotate_triangle_z(triangle)
        #     # tri_rot_z_rot_x = self.rotate_triangle_x(tri_rot_z)
        #     # tri_rot_z_rot_x_trans = self.translate_triangle(tri_rot_z_rot_x)
        #     # tri_rot_z_rot_x_trans_prjct = self.project_triangle(tri_rot_z_rot_x_trans)
        #
        #     triangles.append(tri_rot_z_rot_x_trans_prjct)
        #
        # for triangle in triangles:
        #     draw_triangle(self.screen, triangle)

        for tri in mesh_cube:

            triProjected, triTranslated = Triangle(), Triangle()
            triRotatedZ, triRotatedZX = Triangle(), Triangle()

            for i in range(tri.total_V):
                triRotatedZ.vectors[i] = multiply_matrix_vector_factory(tri.vectors[i], self.mat_rot_z)
                triRotatedZX.vectors[i] = multiply_matrix_vector_factory(triRotatedZ.vectors[i], self.mat_rot_x)

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

            len_norm = sqrt(normal.x ** 2 + normal.y ** 2 + normal.z ** 2) + 5e-7

            normal.x /= len_norm
            normal.y /= len_norm
            normal.z /= len_norm

            if normal.z < 0: pass

            if (normal.x * (triTranslated.vectors[0].x - self.vt_camera.x) +
                    normal.y * (triTranslated.vectors[0].y - self.vt_camera.y) +
                    normal.z * (triTranslated.vectors[0].z - self.vt_camera.z) < 0):

                light_direction = Vec3D((0.0, 0.0, -1.0))

                len_light_direction = sqrt(
                    light_direction.x ** 2 + light_direction.y ** 2 + light_direction.z ** 2) + 5e-7

                light_direction.x /= len_light_direction
                light_direction.y /= len_light_direction
                light_direction.z /= len_light_direction

                light_dp = normal.x * light_direction.x + normal.y * light_direction.y + normal.z * light_direction.z

                # Transform 3d to 2d
                for i in range(tri.total_V):
                    triProjected.vectors[i] = multiply_matrix_vector_factory(triTranslated.vectors[i], self.mat_prjct)
                    # SCALE TO VIEW
                    triProjected.vectors[i].x += 1.0
                    triProjected.vectors[i].y += 1.0

                    triProjected.vectors[i].x *= 0.5 * WIDTH
                    triProjected.vectors[i].y *= 0.5 * WIDTH

                fill_triangle(self.screen, triProjected, color=(25.5 * light_dp * 10, 1 * light_dp * 10, 25.5 * light_dp * 10))

    def translate_triangle(self, triangle: Triangle):

        translation_mat = self.mat_trans
        vector_list: list = []
        # print(triangle, 'LIST')
        # Iterates through each vector
        for vector in triangle.vectors:

            # multiplies it to the translation matrix and appends it to a set vector list.
            vector_list.append(multiply_matrix_vector_factory(vector, translation_mat))
        # print(vector_list, 'DONE')
        return Triangle(vector_list)  # Returns the translated Triangle

    def rotate_triangle_x(self, triangle: Triangle):
        rotation_mat_x = self.mat_rot_x
        vector_list: list = []
        # print(triangle, 'LIST')
        # Iterates through each vector
        for vector in triangle.vectors:

            # multiplies it to the rotation matrix and appends it to a set vector list.
            vector_list.append(multiply_matrix_vector_factory(vector, rotation_mat_x))
        # print(vector_list, 'DONE')
        return Triangle(vector_list)  # Returns the rotated by X-axis Triangle

    def rotate_triangle_z(self, triangle: Triangle):
        rotation_mat_z = self.mat_rot_z
        vector_list: list = []
        # print(triangle, 'LIST')
        # Iterates through each vector
        for vector in triangle.vectors:

            # multiplies it to the rotation matrix and appends it to a set vector list.
            vector_list.append(multiply_matrix_vector_factory(vector, rotation_mat_z))
        # print(vector_list, 'DONE')
        return Triangle(vector_list)  # Returns the rotated by Z-axis Triangle

    def project_triangle(self, triangle: Triangle):
        projection_mat = self.mat_prjct
        vector_list: list = []
        # print(triangle, 'LIST')
        # Iterates through each vector
        for vector in triangle.vectors:

            # multiplies it to the rotation matrix and appends it to a set vector list.
            vector_list.append(multiply_matrix_vector_factory(vector, projection_mat))
        # print(vector_list, 'DONE')
        # Iterates through the projected vectors
        for vector in vector_list:

            # Scaling them into the View/Screen.
            vector.x += 1.0
            vector.y += 1.0

            vector.x *= 0.5 * WIDTH
            vector.y *= 0.5 * WIDTH

        return Triangle(vector_list)  # Returns the projected Triangle

    def run(self):
        while True:
            check_event()
            self.update()
            self.draw()


if __name__ == "__main__":
    ge3d = Game3DEngine()

    # PUBLIC VARIABLES

    cube = Mesh("UnitCube")
    cube.tris(load_from_obj_file('cube.obj', 1.0))

    mesh_cube = cube.triangles

    ge3d.run()
