import os

import kralengine
import pygame

ke = kralengine.KralEngine(debug=True, color="black", size=(1000, 700))

sa = kralengine.Actor(ke, kralengine.IMAGE, kralengine.ResourceLocation("adventurer.png"), (0, 0), kralengine.SIZE(100, 100), (255, 255, 255))
sa.draw()



ke.run()
