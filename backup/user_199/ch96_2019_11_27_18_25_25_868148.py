def update(self):
    self.rect.x += self.speedx
    self.rect.y += self.speedy

    # Mantem dentro da tela
    if self.rect.right > WIDTH:
        self.rect.right = WIDTH
    if self.rect.left < 0:
        self.rect.left = 0
    if self.rect.top < 0:
        self.rect.top = 0
    if self.rect.bottom > HEIGHT:
        self.rect.bottom = HEIGHT