import random
import time

import kralengine
import pygame

ke = kralengine.KralEngine(debug=True, color="blue", size=(1000, 700))

line = kralengine.Line(ke, (255, 255, 255), (0, 0), (50, 100))
# line.draw()

inputs = kralengine.Input(ke)

filter_ = pygame.Surface((ke.width, ke.height))

a = 0

s = pygame.Surface((100, 100))
s.fill((0, 0, 0))
rotated = s
rect = s.get_rect()

elips = kralengine.Actor(ke, "ellipse", (100, 100), (50, 550), (0, 0, 255))
elips.draw()


def update():
    filter_.fill(pygame.color.Color("Grey"))
    # pygame.draw.line(filter_, (0, 0, 0), (0, 0), (x, y))
    pygame.draw.polygon(filter_, (0, 0, 0), [(100, 100), (50, 600), (150, 600)])
    ke.window.blit(filter_, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)



ke.run()
