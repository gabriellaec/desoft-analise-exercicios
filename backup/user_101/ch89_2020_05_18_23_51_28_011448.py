from math import sqrt

class Circulo:
    def __init__(self, c, r):
        self.raio = r
        self.x_centro = c.x
        self.y_centro = c.y
    
    def contem(self, ponto):
        if  sqrt((self.x_centro - ponto.x)**2) <= self.raio and sqrt((self.y_centro - ponto.y)**2) <= self.raio:
            return False
        else:
            return True
    