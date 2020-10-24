import pygame
from random import randint

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

    def mov_qudrado(self, x, y):
        self.movimento=(Quadrado, (x, y))

x = randint(50, 60)
y = randint(50, 60)
x_speed = 2.5
y_speed = 2.5
movimento = Quadrado.mov_qudrado(x, y)

    

pygame.init()
screen = pygame.display.set_mode([LARG,LARG])
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
all_sprites.add(Quadrado())


while True:
    if (x + 10 >= LARG) or (x <= 0):
        x_speed = -x_speed
    if (y +10 >= LARG) or (y <= 0):
        y_speed = -y_speed
    x += x_speed
    y += y_speed
    movimento(x, y)
    clock.tick(60)
    eventos = pygame.event.get()
    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
    