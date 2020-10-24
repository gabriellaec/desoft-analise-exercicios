def movimenta_quadrado(self):
    if self.rect.right > LARG:
        self.rect.right = LARG
    if self.rect.left < -1:
        self.rect.left = -1
        
    