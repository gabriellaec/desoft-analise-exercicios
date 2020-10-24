import pygame

pygame.init()
screen = pygame.display.set_mode((Larg, Larg))
done = False
tem_cor = True
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        screen.fill((0, 0, 0))
        if tem_cor: cor = (0, 128, 255)
        else: cor = (255, 100, 0)
        pygame.draw.rect(screen, cor, pygame.Rect(x, y, 60, 60))
        
        pygame.display.flip()
        clock.tick(60)