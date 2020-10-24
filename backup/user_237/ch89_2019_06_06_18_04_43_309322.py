import math
class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
        
    def contem(self, ponto):
        d = 0.5**((self.centro.y - ponto.y)**2 + (self.centro.x - ponto.x)**2) 
        if d > (self.raio)**2:
            return False
        else:
            return True