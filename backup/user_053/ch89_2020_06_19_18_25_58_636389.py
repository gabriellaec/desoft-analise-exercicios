from math import sqrt
class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    
    def contem(self, ponto):
        self.ponto = ponto
        if (abs(self.ponto - self.centro) > self.raio):
            return True
        else: 
            return False