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
        self.xvel = 1.5
        self.yvel = 1
    
    def update(self):
        if self.rect.x >= LARG - 10:
            self.xvel *= -1
        
        if self.rect.x <= 0:
            self.xvel *= -1
        
        if self.rect.y >= LARG - 10:
            self.yvel *= -1
        
        if self.rect.y <= 0:
            self.yvel *= -1
            
        self.rect.x += self.xvel
        self.rect.y += self.yvel
            

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