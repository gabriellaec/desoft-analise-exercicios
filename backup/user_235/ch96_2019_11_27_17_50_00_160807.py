import pygame

CIANO = (0, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 300
HEIGHT = 300
class Quadrado(pygame.sprite.Sprite):
    def __init__(self):
        super(Quadrado, self).__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(CIANO)
        self.rect = self.image.get_rect()
        self.rect.x = int(WIDTH / 2)
        self.rect.y = int(HEIGHT / 2)
        self.speedx=-2
        self.speedy=-2
        
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Se o carro passar do final da tela, volta para cima
        if self.rect.x > WIDTH or self.rect.x < 0  :
            self.speedx =-self.speedx 
            
        if self.rect.y > HEIGHT or self.rect.y < 0 :
            self.speedy =-self.speedy

pygame.init()
screen = pygame.display.set_mode([WIDTH,HEIGHT])
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