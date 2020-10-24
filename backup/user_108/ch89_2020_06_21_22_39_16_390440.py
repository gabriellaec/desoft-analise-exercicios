from math import sqrt

class Circulo:
    def __init__(self,centro,raio):
        self.centro = centro
        self.raio = raio
        
    def contem(self,ponto):
        distancia = sqrt((centro.x-ponto.x)**2+(centro.y-ponto.y)**2)
        return distancia < raio