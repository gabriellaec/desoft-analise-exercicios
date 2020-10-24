import pygame
import random

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
        self.speedx = 10
        self.speedy = 10
        
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # Se o meteoro passar do final da tela, volta para cima
        if self.rect.top > LARG + 10 or self.rect.left < -25 or self.rect.right > LARG + 20:
            self.rect.x = random.randrange(LARG - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedx = random.randrange(-3, 3)
            self.speedy = random.randrange(2, 9)
            
        


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