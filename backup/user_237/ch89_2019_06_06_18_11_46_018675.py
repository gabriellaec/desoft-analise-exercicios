import math
class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
        
    def contem(self, ponto):
        d = 0.5**((ponto.y - self.centro.y)**2 + (ponto.x - self.centro.x)**2) 
        if self.raio > d:
            return True
        else:
            return False