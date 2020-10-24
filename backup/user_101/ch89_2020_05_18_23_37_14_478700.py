from math import sqrt

class Circulo:
    def __init__(self, c, r):
        self.raio = r
        self.x_centro = c.x
        self.y_centro = c.y
    
    def contem(self, ponto):
        if  (x_centro - ponto.x) <= self.raio and (y_centro - ponto.y) <= self.raio:
            return True
        else:
            return False
    