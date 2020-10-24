import math
class Circulo:
    
    def __init__(self, ponto, raio):
        self.centro = ponto # self.centro.x e self.centro.y
        self.raio = raio
        
    def contem(self, ponto):
        distancia = math.sqrt((self.centro.x - ponto.x)**2 + (self.centro.y - ponto.y)**2)
        if distancia <= self.raio:
            return True
        else:
            return False
