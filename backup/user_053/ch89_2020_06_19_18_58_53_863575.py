from math import sqrt
class Circulo:
    def __init__(self, centro, raio):
        self.centro.x = centro.x
        self.centro.y = centro.y
        self.raio = raio

    def contem(self, ponto):
        dist = sqrt((self.centro.x - ponto.x)**2 + (self.centro.y - ponto.y)**2)
        if dist > self.raio:
            return False
        else:
            return True