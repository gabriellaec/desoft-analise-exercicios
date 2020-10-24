import math

class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio

    def distancia_para(self, ponto):
        return math.sqrt((self.ponto.x - self.centro.x)**2 + (self.ponto.y - self.centro.y)**2)

    def contem(self, ponto):
        if self.centro.distancia_para(ponto) < self.raio:
            return True
        else:
            return False
