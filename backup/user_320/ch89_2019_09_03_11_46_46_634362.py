import math

class Circulo:
    def __init__(self, p1, raio):
        self.p1 = p1
        self.raio = raio
        
    def contem(self, ponto):
        dist =  sqrt(abs(p1.x - ponto.x)** 2 + abs(p1.y - ponto.y) ** 2)
        if dist > self.raio:
            return False
        else:
            return True