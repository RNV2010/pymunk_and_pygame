import pygame as pg

pg.init()
SCREEN = (800, 600)
scr = pg.display.set_mode(SCREEN)
bg_color = (210, 210, 210)
scr.fill(bg_color)
FPS = 60
clock = pg.time.Clock()