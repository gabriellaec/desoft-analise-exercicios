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

        self.speedx = 4
        self.speedy = 4
    
    
    #criado por mim:
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
		
        if self.rect.right > LARG:
            self.speedx = self.speedx*(-1)
        if self.rect.left < 0:
            self.speedx = self.speedx*(-1)
        if self.rect.top < 0:
            self.speedy = self.speedy*(-1)
        if self.rect.bottom > LARG:
            self.speedy = self.speedy*(-1)

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