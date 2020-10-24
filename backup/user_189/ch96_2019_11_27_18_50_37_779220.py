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
        self.speedx = 1
        self.speedy = 0

        

    def update(self):
        if self.rect.x >= LARG:
            self.speedx = -2
            
       
        if self.rect.x <= LARG:
            self.speedx = 2
           
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        print(self.rect.x, self.rect.y)

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