from math import sqrt

class Circulo:
    def __init__(self, c, r):
        self.raio = r
        self.centro = c
        
    def distancia(self, p, outro):
        return distancia
    
    def contem(self, ponto):
        distancia = sqrt((ponto.x - self.centro.x)**2 + (ponto.y - self.centro.y)**2)
        if distancia > self.raio:
            return False
        else:
            return True
    