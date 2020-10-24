import math
class Circulo:
    
    def __init__(self, Centro, Raio):
        self.centro = Centro
        self.raio = float(Raio)
        
    def contem(self, ponto):
        contem = False
        if sqrt(ponto.x**2 + ponto.y**2) <= self.raio:
             contem = True
        return contem