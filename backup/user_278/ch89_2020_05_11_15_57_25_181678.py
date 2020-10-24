from math import sqrt

class Ponto:
    def __init__(self, valor_x, valor_y):
        self.x = valor_x
        self.y = valor_y
        
class Circulo (Ponto):
    def __init__ (self, centro, raio):
        self.c = centro
        self.r = float (raio)
        
    def contem (self, ponto):
        dx = (self.ponto.x - self.c.x)**2
        dy = (self.ponto.y - self.c.y)**2
        d = sqrt(dx+dy)
        if (d < self.r):
            True