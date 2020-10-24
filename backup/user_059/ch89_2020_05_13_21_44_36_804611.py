import math

class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio

    def distancia_para(self, ponto):
        return math.sqrt((self.ponto - self.centro)**2 + (self.ponto - self.centro)**2)

    def contem(self, ponto):
        if self.distancia_para(ponto) < self.raio:
            return True
        else:
            return False
