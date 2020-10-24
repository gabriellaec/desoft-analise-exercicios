import math
class Circulo:
    
    def __init__(self, Centro, Raio):
        self.centro = Centro
        self.raio = float(Raio)
        
    def contem(self, ponto):
        contem = False
        self.distanciaX = abs(ponto.x**2 - self.centro.x**2)
        self.distanciaY = abs(ponto.y**2 - self.centro.y**2)
        if math.sqrt(self.distanciaX + self.distanciaY) <= self.raio:
             contem = True
        return contem