from math import sqrt

class Ponto:
    def distance_to(self, ponto2):
        return sqrt((self.x - self.ponto2.x)**2 + (self.y - self.ponto2.y)**2)

class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    def contem(self, ponto):
        if self.centro.distance_to(ponto) > self.raio:
            return True
        else:
            return False
