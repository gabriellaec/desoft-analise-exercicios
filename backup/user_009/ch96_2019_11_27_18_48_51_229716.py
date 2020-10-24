import pygame

import pygame, random

CIANO = (0, 255, 255)
BLACK = (0, 0, 0)
LARG = 300

class Quadrado(pygame.sprite.Sprite):
    def __init__(self):
        super(Quadrado, self).__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(CIANO)
        self.rect = self.image.get_rect()
        self.rect.center = (LARG/2, LARG/2)
        self.velx = random.randint(2,3)
        self.vely = random.randint(1,3)
        self.rect.x = random.randint(0,LARG)
        self.rect.y = random.randint(0,LARG)

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely

        if self.rect.x ==  LARG or self.rect.x == 0:
            self.velx = -self.velx
        if self.rect.y ==  LARG or self.rect.y == 0:
            self.vely = -self.vely    



