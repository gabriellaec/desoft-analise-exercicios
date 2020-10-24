import math
class Circulo:
    
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
        
    def contem(self, ponto):
        d = math.sqrt((self.centro.x - self.ponto.x) ** 2 + (self.centro.y - self.ponto.y) ** 2)
        if d < self.raio:
            return True
        else:
            return False