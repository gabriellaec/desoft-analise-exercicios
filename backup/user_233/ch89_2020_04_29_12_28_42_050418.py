from math import sqrt

class Circulo:
    
    def __init__(self, ponto, raio):
        self.ponto = ponto
        self.raio = raio
        
    def contem(self, ponto):
        
        delta_y = self.ponto.y - ponto.y
        delta_x = self.ponto.x - ponto.x
        distancia = sqrt(delta_x ** 2 + delta_y ** 2)
        
        return distancia <= self.raio
        
        
        
        
        