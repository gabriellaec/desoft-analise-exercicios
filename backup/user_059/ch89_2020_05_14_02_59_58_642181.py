import math

class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio

    def contem(self, ponto):
        self.ponto = ponto
        x = math.sqrt((self.ponto.x - self.centro.x)**2 + (self.ponto.y - self.centro.y)**2)
        if x < self.raio:
            return True
        else:
            return False
