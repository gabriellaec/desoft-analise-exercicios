from math import sqrt

class Circulo:
    def __init__(self, c, r):
        self.raio = r
        self.centro = c
        
    def distance_to(self, outro_ponto):
        distancia = sqrt((self.centro.x - outro_ponto.x)**2 + (self.centro.y - outro_ponto.y)**2)
        return distancia
    
    def contem(self, ponto):
        if distance_to(ponto) > self.raio:  
            return False
        else:
            return True
    