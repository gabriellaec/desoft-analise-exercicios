import pygame
 
CIANO = (0, 255, 255)
BLACK = (0, 0, 0)
LARG = 300
 
pygame.init()
screen = pygame.display.set_mode([LARG,LARG])
clock = pygame.time.Clock()
quadrado_x = 25
velocidade_x = 1
quadrado_y = 25
velocidade_y = 1
 
while True:
    quadrado_x += velocidade_x
    quadrado_y += velocidade_y
    if quadrado_y > LARG-30 or quadrado_y < 0:
        velocidade_y = velocidade_y * -1
    if quadrado_x > LARG-30 or quadrado_x < 0:
        velocidade_x = velocidade_x * -1
    screen.fill(BLACK)
    pygame.draw.rect(screen, CIANO, [quadrado_x, quadrado_y, 25, 25])
    clock.tick(60)
    pygame.display.flip()