from math import sqrt

class Circulo:
    def __init__(self, c, r):
        self.raio = r
        self.centro = c
        
    def distance_to(self, ponto, outro_ponto):
        distancia = sqrt((ponto.x - outro_ponto.x)**2 + (ponto.y - outro_ponto.y)**2)
        return distancia
    
    def contem(self, ponto):
        if distance_to(self.centro, ponto) > self.raio:  
            return False
        else:
            return True
    