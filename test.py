from settings import *
import pygame as pg


def check_event():
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.type == pg.K_ESCAPE):
            pg.quit()
            sys.exit()

def update(clock):
    pg.display.flip()
    clock.tick(FPS)
    pg.display.set_caption(f'{clock.get_fps():.1f}')

def DrawTriangle(surface, values , color = 0x2588):

    x1 , y1 , x2 , y2 , x3 , y3 = values
    
    pg.draw.aaline(surface, color, (x1, y1), (x2, y2))
    pg.draw.aaline(surface, color, (x2, y2), (x3, y3))
    pg.draw.aaline(surface, color, (x3, y3), (x1, y1))

    

def run(clock, values):
        
    while True:
        check_event()
        update(clock)
        DrawTriangle(pyscreen, values, 'white')

triangle1 = [[0.0, 0.0, 0.0],   [0.0, 1.0, 0.0],    [1.0, 1.0, 0.0]]
triangle2 = [[0.0, 0.0, 0.0],   [1.0, 1.0, 0.0],    [1.0, 0.0, 0.0]]
triangle3 = [[1.0, 0.0, 0.0],   [0.0, 1.0, 0.0],    [1.0, 1.0, 0.0]]
# triangle3 = triangle1[0][0:2]+triangle1[1][0:2]+triangle1[2][0:2]

# for idx, point in enumerate(triangle3):
#     triangle3[idx] = (triangle3[idx] + 1)* (0.5 * WIDTH)
    

# pg.init()
# screen = pg.display.set_mode(RES)
# clock = pg.time.Clock()
# pyscreen = pg.display.set_mode(RES)

list1 = [triangle1, triangle2, triangle3]


list2 = sorted(list1, key = lambda x: x > 5)

print(list2)