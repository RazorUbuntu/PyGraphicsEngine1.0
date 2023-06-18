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


class Game3DEngine:  # The main class to start the Engine

    def __init__(self):  # Initialize the minimum requirements
        # Pygame init func
        pg.init()

        # Deploy the Screen: TODO: Use Screen3D class
        self.screen = pg.display.set_mode(RES)

        # An object to help keep track of time
        self.clock = pg.time.Clock()
        self.current_time = self.clock.get_time() / 100

    def update(self):  # Update the screen every call
        # Update the entire screen
        pg.display.flip()

        # Update the screen to this number of FramesPerSecond
        self.clock.tick(FPS)

        # Show FPS next to the Icon
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')
        self.current_time = self.clock.get_time() / 100

    def draw(self):
        self.screen.fill('black')

    def run(self):

        while True:
            check_event()
            self.update()
            self.draw()


if __name__ == "__main__":
    ge3d = Game3DEngine()
    ge3d.run()
