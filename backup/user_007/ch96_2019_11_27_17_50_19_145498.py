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
    def move(self):
        if self.rect.center[0] == LARG or self.rect.center[1] == LARG or self.rect.center[0] == -LARG or self.rect.center[1] == -LARG:
            self.rect.center = (self.rect.center[0]+1,self.rect.center[1]-2)
        else:
            self.rect.center = (self.rect.center[0]+1,self.rect.center[1]+2)


pygame.init()
screen = pygame.display.set_mode([LARG,LARG])
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
q = Quadrado()
all_sprites.add(q)
moviment = 'straight'

while True:
    clock.tick(60)
    if moviment == 'straight':
      q.move()
    eventos = pygame.event.get()
    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
