def __init__(self):
    self.speedx = 5
    self.speedy = 5
    if self.rect.x == 10:
        self.speedx = -5
    elif self.rect.x == 0:
        self.speedx = 5
    elif self.rect.y == 10:
        self.speedy = -5
    elif self.rect.y == 0:
        self.speedy = 5
