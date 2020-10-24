def __init__(self, ):
    
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(-300, -10)
        self.rect.x = random.randrange(0, screen_width)
 