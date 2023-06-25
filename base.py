# INFO: STABLE RELEASE v1.0
# This is the base script that runs the screen and the given objects, physics, scripts etc.


###############################
#         Self Imports        #
###############################

from functions import *
from type_classes import Mesh
from SETTINGS import *

###############################
#           Imports           #
###############################

import pygame as pg
import sys
from time import time


###############################
#            Begin            #
###############################




def draw_triangles(surface, triangles):
    for triangle in triangles:
        fill_triangle(surface, triangle, color='white')
        draw_triangle(surface, triangle, color='black', width=2.0)


class Game3DEngine:  # The main class to start the Engine

    def __init__(self):  # Initialize the minimum requirements

        # PRIVATE VARIABLES: FIXED
        # -------------------------------------------------------------------------------------- #
        self.mat_prjct      : np.ndarray = projection_matrix(f_aspect_ratio, f_fov_rad, f_far, f_near)
        self.mat_trans      : np.ndarray = translation_matrix(x=0.0, y=0.0, z=15.0)
        self.mat_ident      : np.ndarray = identity_matrix()

        self.vt_camera      : Vec3D      = Vec3D()
        self.look_dir       : Vec3D      = Vec3D((0,0,1))

        self.f_theta        : float      = 0.0
        self.mat_rot_z      : np.ndarray = identity_matrix()
        self.mat_rot_x      : np.ndarray = identity_matrix()
        self.mat_world      : np.ndarray = identity_matrix()
        self.light_direction: Vec3D      = Vec3D((0.0, 0.0, -1.0))

        self.v_upward       : Vec3D      = Vec3D((0, 1, 0))
        self.v_target       : Vec3D      = self.vt_camera + self.look_dir
        self.mat_camera     : np.ndarray = point_at_matrix(self.vt_camera, self.v_target, self.v_upward)

        self.mat_view       : np.ndarray = quick_inverse(self.mat_camera)
        # -------------------------------------------------------------------------------------- #

        # Pygame init func
        pg.init()

        # Deploy the Screen: TODO: Use Screen3D class
        self.screen = pg.display.set_mode(RES)

        # An object to help keep track of time
        self.clock = pg.time.Clock()
        self.init_time = time()
        self.current_time = None

    def update(self, alpha_speed=1.0):  # Update the screen every call

        # Update the entire screen
        pg.display.flip()

        # Update the screen to this number of Frames-Per-Second
        self.clock.tick(FPS)

        # Show FPS next to the Icon
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')
        self.current_time = time() - self.init_time

        # # Changing angle value as the axis rotates.
        # self.f_theta = self.current_time * alpha_speed

        # Updating the rotational matrices with the new theta value.
        self.mat_rot_z = rotation_matrix_z(self.f_theta)
        self.mat_rot_x = rotation_matrix_x(self.f_theta)

        self.mat_world = self.mat_rot_z * self.mat_rot_x * self.mat_trans

    def check_event(self):  # Check for User Input / an Event
        # Event loop
        for event in pg.event.get():

            # Exit the Engine if either escape or the quit button is pressed.
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.type == pg.K_ESCAPE):
                # End the PyGame instance
                pg.quit()

                # Exit the interpreter
                sys.exit()
            if event.type == pg.K_w: 
                self.vt_camera.y += 8.0 * self.current_time
            
            if event.type == pg.K_s: 
                self.vt_camera.y -= 8.0 * self.current_time

    def draw_triangles(self):  # Draw triangles on the screen.

        # clear the screen
        self.screen.fill('black')
        triangles: list = []

        # iterate through every triangle in the model.
        for triangle in mesh:

            # rotate that face by the Z-axis
            tri_rot_z = self.rotate_triangle_z(triangle)

            # rotate that face by the X-axis
            tri_rot_z_rot_x = self.rotate_triangle_x(tri_rot_z)

            # move that face through space
            tri_rot_z_rot_x_trans = self.translate_triangle(tri_rot_z_rot_x)

            # find the vector lines of the triangle to find their face's normal
            line_1 = tri_rot_z_rot_x_trans.vectors[0] - tri_rot_z_rot_x_trans.vectors[1]
            line_2 = tri_rot_z_rot_x_trans.vectors[0] - tri_rot_z_rot_x_trans.vectors[2]

            # Cross Product of two vector lines is their normal
            normal = cross_product(line_1, line_2)

            # Normalizing the Normal
            len_normal = vector_length(normal)
            normal.div(len_normal)

            # if the face is not in view, do not render it.
            if dot_product(normal, (tri_rot_z_rot_x_trans.vectors[0] - self.vt_camera)) < 0:

                tri_view = self.view_triangle(tri_rot_z_rot_x_trans)
                
                # project 3d to 2d:
                tri_rot_z_rot_x_trans_prjct = self.project_triangle(tri_view)

                # Normalizing the directional light.
                len_light_direction = vector_length(self.light_direction)
                self.light_direction.div(len_light_direction)

                # Calculating the lighting and setting the face's lighting to it.
                tri_rot_z_rot_x_trans_prjct.lighting = dot_product(normal, self.light_direction)

                # Add the triangles to the list for sorting.
                triangles.append(tri_rot_z_rot_x_trans_prjct)

        # Iterate through each triangle and get them drawn on the screen
        for triangle in triangles:
            lit_fill_color = mul_seq_const2tup(colors['white'], triangle.lighting)

            # draws a filled triangle on the screen.
            fill_triangle(self.screen, triangle, color=lit_fill_color)

            # # draws the outline of the triangle on the screen.
            # draw_triangle(self.screen, triangle, color='black', width=1)

    # Move a triangle in 3D space.
    def translate_triangle(self, triangle: Triangle):

        translation_mat = self.mat_trans
        vector_list: list = []

        # Iterates through each vector
        for vector in triangle.vectors:
            # multiplies it to the translation matrix and appends it to a set vector list.
            vector_list.append(multiply_matrix_vector_factory(vector, translation_mat))

        return Triangle(vector_list)  # Returns the translated Triangle

    # Rotate a triangle around its X-axis
    def rotate_triangle_x(self, triangle: Triangle):
        rotation_mat_x = self.mat_rot_x
        vector_list: list = []

        # Iterates through each vector
        for vector in triangle.vectors:
            # multiplies it to the rotation matrix and appends it to a set vector list.
            vector_list.append(multiply_matrix_vector_factory(vector, rotation_mat_x))

        return Triangle(vector_list)  # Returns the rotated by X-axis Triangle

    # Rotate a triangle around its Z-axis
    def rotate_triangle_z(self, triangle: Triangle):
        rotation_mat_z = self.mat_rot_z
        vector_list: list = []

        # Iterates through each vector
        for vector in triangle.vectors:
            # multiplies it to the rotation matrix and appends it to a set vector list.
            vector_list.append(multiply_matrix_vector_factory(vector, rotation_mat_z))

        return Triangle(vector_list)  # Returns the rotated by Z-axis Triangle

    # Project a triangle to the View/Screen
    def project_triangle(self, triangle: Triangle):
        projection_mat = self.mat_prjct
        vector_list: list = []

        # Iterates through each vector
        for vector in triangle.vectors:
            # multiplies it to the projection matrix and appends it to a set vector list.
            vector_list.append(multiply_matrix_vector_factory(vector, projection_mat))

        # Iterates through the projected vectors
        for vector in vector_list:
            # Scaling them into the View/Screen.
            vector.x += 1.0
            vector.y += 1.0

            vector.x *= 0.5 * WIDTH
            vector.y *= 0.5 * WIDTH

        return Triangle(vector_list)  # Returns the projected Triangle

    def view_triangle(self, triangle: Triangle):
        view_mat = self.mat_view
        vector_list: list = []

        # Iterates through each vector
        for vector in triangle.vectors:
            # multiplies it to the view matrix and appends it to a set vector list.
            out_vec = multiply_matrix_vector_factory(vector, view_mat)
            vector_list.append(out_vec.div(out_vec.w))

        return Triangle(vector_list)  # Returns the View Triangle

    # World matrix optimizes all the calculations to be done only once with this matrix.
    def world_triangle(self, triangle: Triangle):

        world_mat = self.mat_world
        vector_list: list = []

        # Iterates through each vector
        for vector in triangle.vectors:
            # multiplies it to the world matrix and appends it to a set vector list.
            vector_list.append(multiply_matrix_vector_factory(vector, world_mat))

        # Iterates through the transformed vectors
        for vector in vector_list:
            # Scaling them into the View/Screen.
            vector.x += 1.0
            vector.y += 1.0

            vector.x *= 0.5 * WIDTH
            vector.y *= 0.5 * WIDTH

        return Triangle(vector_list)  # Returns the transformed Triangle

    def run(self):  # Starts all the Functions
        while True:
            self.check_event()               # Check for user input
            self.update()               # Update data
            self.draw_triangles()       # Draw visuals


if __name__ == "__main__":
    ge3d = Game3DEngine()

    # PUBLIC VARIABLES

    axis = Mesh("Unitaxis")
    axis.tris(load_from_obj_file('axis.obj', 1.0))
    mesh = axis()

    ge3d.run()
