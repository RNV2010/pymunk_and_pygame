import pygame as pg
import pymunk as pm
import pymunk.pygame_util
import setting
from pygame.locals import *

pymunk.pygame_util.positive_y_is_up = False
draw_options = pymunk.pygame_util.DrawOptions(setting.scr)
C_FONT = pg.font.SysFont('Kristen ITC', 32)

space = pm.Space()
space.gravity = 0, 500
draw_options = pymunk.pygame_util.DrawOptions(setting.scr)

count_green = 0


def print_count(count: int) -> tuple:
    count_text = C_FONT.render(str(count), True, 'black', (175, 175, 175))
    count_area = count_text.get_rect()
    count_area.topleft = (25, 30)
    return count_text, count_area


def rect(x: int, y: int, screen=setting.scr) -> tuple:
    model = pg.Rect(x, y, 100, 100)
    color = 'yellow'
    result = (screen, color , model)
    return result




def create_ball(space, pos: tuple[int, int], mass: int = 10, radius: int = 100,
                color: tuple[int, int, int, int] = (255, 0, 0, 0)):
    moment = pm.moment_for_circle(mass, 0, radius)
    body = pm.Body(mass, moment)
    body.position = pos
    shape = pm.Circle(body, radius)
    shape.elasticity = 1
    shape.friction = 0.7
    shape.color = color
    space.add(body, shape)
    return body

def create_floor(space):
    body = pm.Body(body_type=pm.Body.STATIC)
    floor_1 = pm.Segment(body, (0, setting.height - 400), (setting.width - 200, setting.height), 10)
    floor_2 = pm.Segment(body, (setting.width, setting.height - 400), (setting.width - 200, setting.height), 10)
    floor_1.elasticity = 0.5
    floor_2.elasticity = 0.5
    space.add(body, floor_1, floor_2)







create_floor(space)
x1, y1 = 100, 100
person = create_ball(space, (setting.SCREEN[0] - 150, 150), 10, 50, (75, 0, 130, 0))




while True:
    setting.scr.fill(setting.bg_color)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        person.apply_force_at_local_point((0, -5000), (0, 0))
    if keys[pg.K_DOWN]:
        person.apply_force_at_local_point((0, 5000), (0, 0))
    if keys[K_LEFT]:
        person.apply_force_at_local_point((-5000, 0), (0, 0))
    if keys[K_RIGHT]:
        person.apply_force_at_local_point((5000, 0), (0, 0))
    if keys[K_z]:
        space = pm.Space()
        space.gravity = 0, 2000
        create_floor(space)
        count_green = 0
    mouse = pg.mouse.get_pressed()
    pos = pg.mouse.get_pos()
    if mouse[0]:
        create_ball(space, pos, radius=40)
    if mouse[2]:
        create_ball(space, pos, 50, 10, (0, 255, 0, 150))
        count_green += 1
    if keys[K_q]:
        create_ball(space, pos, 50, 10, (255, 99, 71, 0))

    space.step(1 / setting.FPS)
    space.debug_draw(draw_options)
    setting.scr.blit(*print_count(count_green))

    pg.display.flip()
    setting.clock.tick(setting.FPS)

