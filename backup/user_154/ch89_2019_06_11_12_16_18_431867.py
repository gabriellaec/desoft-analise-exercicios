from math import sqrt

class Circulo:
    
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    
    def contem(self, ponto):
        distancia_x = abs(ponto.x - self.centro.x)
        distancia_y = abs(ponto.y - self.centro.y)
        
        return self.raio <= srqt(distancia_x**2 + distancia_y**2)