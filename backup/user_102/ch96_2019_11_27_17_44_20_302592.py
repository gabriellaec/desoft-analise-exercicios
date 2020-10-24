def move(self):
    self.rect.x= LARG
    self.rect.y = LARG
    self.speedx = 3
    self.speedy = 3
    if self.rect.right > LARG:
        self.rect.right = LARG
    if self.rect.left < 0:
        self.rect.left = LARG
    if self.rect.top > LARG:
        self.rect.top = LARG
    if self.rect.bottom < 0:
        self.rect.bottom = LARG