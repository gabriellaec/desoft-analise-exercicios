collisions = pygame.sprite.spritecollide(self, self.blocks, False)
for collision in collisions:
     if self.speedy > 0:
            self.rect.bottom = collision.rect.top
            self.speedy = 0
    elif self.speedy < 0:
        self.rect.top = collision.rect.bottom
        self.speedy = 0
        
    if self.speedx > 0:
        self.rect.right = collision.rect.left
    elif self.speedx < 0:
        self.rect.left = collision.rect.right