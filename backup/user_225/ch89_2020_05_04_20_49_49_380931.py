import math
class Circulo:
    def __init__(self, centro,raio):
        self.centro = centro
        self.raio = raio
    def contem(self, ponto):
        d = ((ponto.y-self.centro.y)**2 + (ponto.x-self.centro.x)**2)**0.5
        if d > self.raio:
            return False
        else:
            return True
        
    