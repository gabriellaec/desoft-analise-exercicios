class Ponto:
    def __init__(self, valor_x, valor_y):
        self.x = valor_x
        self.y = valor_y
        
class Circulo (Ponto,ponto):
    def __init__ (self, centro, raio):
        self.c = centro
        self.r = float (raio)
    def contem (self, ponto):
        dx = self.ponto.x - self.c.x
        dy = self.ponto.y - self.c.y
        if (dx < raio) and (dy < raio):
            True