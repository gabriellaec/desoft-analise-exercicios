import math
class Circulo:
    
    def __init__(self, Centro, Raio):
        self.centro = Centro
        self.raio = float(Raio)
        
    def contem(self, ponto):
        contem = False
        self.distanciaX = (ponto.x - self.centro.x)**2
        self.distanciaY = (ponto.y - self.centro.y)**2
        if math.sqrt(self.distanciaX + self.distanciaY) <= self.raio:
             contem = True
        return contem