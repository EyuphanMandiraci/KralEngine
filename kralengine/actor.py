import pygame
from kralengine import KralEngine


class Actor:
    def __init__(self, window: KralEngine, shape=None,
                 size=(100, 100), pos=(0, 0), color=(0, 0, 0), atype="object", image=None):

        self.window = window
        self.shape = shape
        self.size = size
        self.width = self.size[0]
        self.height = self.size[1]
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.color = color
        self.type = atype
        self.image = image

        self.drawed = False

        if image is not None:
            self.image = pygame.image.load(image)
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
            if self.size == "image":
                self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
                self.image = pygame.transform.scale(self.image, self.image.get_size())
        if hasattr(self.window, "objects"):
            self.window.objects.append(self)

    def draw(self):
        self.drawed = True
        if self.type == "object":
            if self.size == "image":
                if self.window.debug:
                    print("DEBUG - ACTOR: Size is undefined!")
            else:
                rect = pygame.Rect(self.x, self.y, self.width, self.height)
                if self.shape == "rect":
                    if hasattr(self.window, "window"):
                        pygame.draw.rect(self.window.window, self.color, rect)
                    else:
                        pygame.draw.rect(self.window, self.color, rect)
                elif self.shape == "ellipse":
                    if hasattr(self.window, "window"):
                        pygame.draw.ellipse(self.window.window, self.color, rect)
                    else:
                        pygame.draw.ellipse(self.window, self.color, rect)
                else:
                    if self.window.debug:
                        print(f"DEBUG - ACTOR: Incorrect shape. Shape can "
                              f"be 'rect' or 'ellipse'. Your shape is '{self.shape}'!")
        elif self.type == "sprite":
            if self.image is None:
                if self.window.debug:
                    print("DEBUG - ACTOR: Image is undefined!")
            else:
                self.window.window.blit(self.image, self.pos)

    def update(self):
        self.pos = [self.x, self.y]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.drawed:
            self.draw()
