from math import *
class Circulo:
    def __init__(self, ptc, raio):
        self.ptc = ptc
        self.raio = raio

    def contem(self, ponto):
        a = sqrt((self.ptc.x - ponto.x)**2 +(self.ptc.y - ponto.y)**2)
        if a < self.raio:
            return True
        else:
            return False