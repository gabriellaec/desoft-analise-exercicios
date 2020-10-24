def update(self):
    self.rect.x += self.speedx
    self.rect.y += self.speedy
    if self.rect.right >= LARG:
    	self.speedx=-self.speedx
    if self.rect.left <= 0:
        self.speedx=-self.speedx
    if self.rect.left < 0:
        self.rect.left = 0
    if self.rect.bottom > LARG:
        self.speedy=-self.speedy
    if self.rect.top < 0:
        self.speedy=-self.speedy