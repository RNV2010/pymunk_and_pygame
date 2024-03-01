import pygame as pg
import pymunk as pm
import pymunk.pygame_util
import setting
from pygame.locals import *

pymunk.pygame_util.positive_y_is_up = False
draw_options = pymunk.pygame_util.DrawOptions(setting.scr)

space = pm.Space()
space.gravity = 0, 2000



def rect(x: int, y: int, screen=setting.scr) -> tuple:
    model = pg.Rect(x, y, 100, 100)
    color = 'yellow'
    result = (screen, color , model)
    return result


def circle(x: int, y: int, screen=setting.scr):
    radius = 50
    center = (x + radius / 2, y + radius / 2)
    width = 5
    color = 'blue'
    result = (screen, color, center, radius, width)
    return result

















x1, y1 = 100, 100
x2, y2 = setting.SCREEN[0] - 150, 150
while True:
    setting.scr.fill(setting.bg_color)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    keys = pg.key.get_pressed()
    if keys[K_UP]:
        y1 -= 3
    if keys[K_DOWN]:
        y1 += 3
    if keys[K_LEFT]:
        x1 -= 3
    if keys[K_RIGHT]:
        x1 += 3
    if keys[K_w]:
        y2 -= 3
    if keys[K_s]:
        y2 += 3
    if keys[K_d]:
        x2 += 3
    if keys[K_a]:
        x2 -= 3

    # sqare = rect(x1, y1)
    pg.draw.rect(*rect(x1, y1))
    pg.draw.circle(*circle(x2, y2))

    pg.display.flip()
    setting.clock.tick(setting.FPS)

