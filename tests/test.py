import os
import pprint

import kralengine
import pygame
import pygame.gfxdraw
import time
from reportlab.lib import colors


ke = kralengine.KralEngine(debug=True, color="red", size=(1000, 700))
# Make True this if you want skip splashscreen
ke.splashscreendone = True
# Delete this if you dont want light
ke.light_init()

sa = kralengine.Actor(ke, kralengine.IMAGE, kralengine.ResourceLocation("adventurer.png"), (54, 342),
                      kralengine.SIZE(100, 100), (255, 255, 255))
sa.draw()

light = kralengine.PointLight(ke, 500, 350, (500, 200), (255, 255, 255))
light.draw()


line = kralengine.Line(ke, (255, 255, 255), (500, 0), (500, 400))
# line.draw()


anim = kralengine.SpriteAnimation("idle", "idle1", 0.1)
walk_anim = kralengine.SpriteAnimation("walk", "walk", 0.1)

sa.addSpriteAnimation("idle", anim)

sa.addSpriteAnimation("walkr", walk_anim)
sa.addSpriteAnimation("walkl", walk_anim, True, False)

keys = kralengine.Input(ke)

anim = False


coloranim = kralengine.ColorAnimation((255, 0, 0), (0, 0, 255), 1)

s = kralengine.Actor(ke, kralengine.OBJECT, kralengine.RECT, (0, 0), kralengine.SIZE(100, 100), (255, 255, 255))
# s.draw()

s.addColorAnimation("sample", coloranim)
s.playAnimation("sample")

t = kralengine.Text(ke, color=(255, 255, 255))
# t.write()


def colorRanger(c0, c1, n):
    temp = []
    if n == 1: return [c0]

    if n > 1:
        lim = n - 1
        for i in range(n):
            temp.append(colors.linearlyInterpolatedColor(c0, c1, 0, lim, i))
    return temp



surf = pygame.Surface((ke.width, 401), pygame.SRCALPHA)

cr = colorRanger(colors.Color(0, 0, 0, 255), colors.Color(0, 0, 0, 0), surf.get_height())
cr_ = []
for i in cr:
    cr_.append(i.rgba())
cr = cr_
del cr_


# filter_ = pygame.Surface((ke.width, ke.height))



def update():
    global anim, sa, surf, ke, cr
    if keys.get_key_pressed(keys.keys["D"]):
        # anim = "r"
        # sa.pos[0] += 1
        light.pivot[0] += 2
    elif keys.get_key_pressed(keys.keys["A"]):
        # anim = "l"
        # sa.pos[0] -= 1
        light.pivot[0] -= 2
    elif keys.get_key_pressed(keys.keys["W"]):
        # anim = "l"
        # sa.pos[0] -= 1
        light.pivot[1] -= 2
    elif keys.get_key_pressed(keys.keys["S"]):
        # anim = "l"
        # sa.pos[0] -= 1
        light.pivot[1] += 2
    else:
        anim = False

    if keys.get_key_pressed(keys.keys["F"]):
        light.width += 5
    elif keys.get_key_pressed(keys.keys["G"]):
        light.width -= 5

    if keys.get_key_pressed(keys.keys["H"]):
        light.height += 5
    elif keys.get_key_pressed(keys.keys["J"]):
        light.height -= 5
    if keys.get_key_pressed(keys.keys["UP"]):
        # sa.pos[1] -= 1
        light.angle += 1
    elif keys.get_key_pressed(keys.keys["DOWN"]):
        # sa.pos[1] += 1
        light.angle -= 1
    # if anim == "l":
    #     sa.playAnimation("walkl")
    # elif anim == "r":
    #     sa.playAnimation("walkr")
    # else:
    #     sa.playAnimation("idle")
    # pygame.draw.rect(ke.light_surf, (0, 0, 0), (100, 100, 31, 31))
    # ke.light_surf.blit(pygame.Surface((100, 100)), (0, 0))
    # for index, i in enumerate(range(surf.get_height())):
    #     pygame.gfxdraw.line(surf, 0, i, surf.get_width(), i, cr[index])
    # filter_.fill("White")
    # pygame.gfxdraw.textured_polygon(filter_, ((100, 100), (50, 400), (150, 400)), surf, 0, 0)
    # ke.window.blit(filter_, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
    # pygame.draw.polygon(ke.window, (255, 255, 255), ((0, 0), (0, 100), (200, 200)))


ke.run()

# TODO: Light improve
# TODO: Animation improve
# TODO: More object type
