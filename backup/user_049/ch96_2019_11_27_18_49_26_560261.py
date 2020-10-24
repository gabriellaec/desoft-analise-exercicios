import sys, pygame
pygame.init()

LARG = 300
speed = [3, 1]
CIANO = (0, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((LARG,LARG))
clock = pygame.time.Clock()
FPS = 60

ball = pygame.Surface((30,30)).convert()
ball.fill(CIANO)
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > LARG:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > LARG:
        speed[1] = -speed[1]

    screen.fill(BLACK)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    clock.tick(FPS)