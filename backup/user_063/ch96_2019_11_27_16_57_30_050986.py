import pygame as py

CIANO = (0,255,255)
BLACK = (0,0,0)
LARG = 300

class Quadrado(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.Surface((10,10))
        self.image.fill(CIANO)
        self.rect = self.image.get_rect()
        self.rect.center = (LARG/2, LARG/2)
        self.speedx = 2
        self.speedy = 1
        
    def update(self):
        if self.rect.left < 0:
            self.speedx = -self.speedx
        elif self.rect.right >= LARG:
            self.speedx = -self.speedx
        if self.rect.top <= 0:
            self.speedy = -self.speedy
        elif self.rect.bottom >= LARG:
            self.speedy = -self.speedy
            
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        
py.init()
screen = py.display.set_mode([LARG,LARG])
clock = py.time.Clock()
all_sprites = py.sprite.Group()
all_sprites.add(Quadrado())

while True:
    clock.tick(60)
    eventos = py.event.get()
    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    py.display.flip()