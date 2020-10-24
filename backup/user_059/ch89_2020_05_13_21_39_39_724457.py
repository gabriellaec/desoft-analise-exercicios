import math

class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio

    def distancia_para(self, ponto):
        self.ponto = ponto
        return math.sqrt((self.ponto.x - self.centro)**2 + (self.ponto.y - self.centro)**2)

    def contem(self, ponto):
        if self.distancia_para(ponto) < self.raio:
            return True
        else:
            return False
