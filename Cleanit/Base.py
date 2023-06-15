# INFO:
# This is the base script that runs the screen and the given objects, physics, scripts etc.


###############################
#         Self Imports        #
###############################

from type_classes import *
from Errors import *

###############################
#           Imports           #
###############################

import pygame as PG
import sys
from math import sqrt

###############################
#            Begin            #
###############################

class Game3DEngine: # The main class to start the Engine

    def __init__(self, screen): # Initialize the mimum reqs
        # Pygame init func
        PG.init()

        # Deploy the Screen
        self.screen = screen.Screen

        # An object to help keep track of time
        self.clock = PG.time.Clock()

    def Update(self): # Update the screen every call
        # Update the entire screen
        PG.display.flip() 

        # Update the screen to this number of FramesPerSecond
        self.clock.tick(FPS) 

        # Show FPS next to the Icon
        PG.display.set_caption(f'{self.clock.get_fps():.1f}')
        self.current_time = self.clock.get_time()/100

    def CheckEvent(self): # Check for User Input / an Event
        # Event loop
        for event in PG.event.get():

            # Exit the Engine if either escape or the quit button is pressed.
            if event.type == PG.QUIT or (event.type == PG.KEYDOWN and event.type == PG.K_ESCAPE):

                # End the PyGame instance
                PG.quit()

                # Exit the interpreter
                sys.exit()
    def Run(self):
        pass

if __name__ == "__main__":

    pass
