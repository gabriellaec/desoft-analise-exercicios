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
        self.rect.center = (LARG/2, LARG/2)
        
    def update(self):
        self.rect.x += self.speedx
        

pygame.init()
screen = pygame.display.set_mode([LARG,LARG])
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
all_sprites.add(Quadrado())

while True:
    Quadrado.speedx = 8
    
    hits = pygame.sprite.spritecollide(Quadrado, LARG, False, pygame.sprite.collide)
    if hits:
        Quadrado.speedx = -8
    hits = pygame.sprite.spritecollide(Quadrado, -LARG, False, pygame.sprite.collide)
    if hits:
        Quadrado.speedx = +8
    clock.tick(60)
    eventos = pygame.event.get()
    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()   