import random
import pygame

CIANO = (0, 255, 255)
BLACK = (0, 0, 0)
LARG = 300

class Quadrado(pygame.sprite.Sprite):
    def __init__(self):
        super(Quadrado, self).__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(CIANO)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARG/2
        self.rect.centery = LARG/2
        self.speedx = random.randint(-3,3)
        self.speedy = random.randint(-3,3)
    def update(self):
        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy
        if self.rect.centerx >= LARG:
            self.speedx = random.randint(-3,-1)
        elif self.rect.centerx <= 0:
            self.speedx = random.randint(1,3)
            self.rect.center 
        elif self.rect.centery >= LARG:
            self.speedy = random.randint(-3,-1)
        elif self.rect.centery <= 0:
            self.speedy = random.randint(1,3)

pygame.init()
screen = pygame.display.set_mode([LARG,LARG])
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
all_sprites.add(Quadrado())

while True:
    clock.tick(60)
    eventos = pygame.event.get()
    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
    
    all_sprites.update()