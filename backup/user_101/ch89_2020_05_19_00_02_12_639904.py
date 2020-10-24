from math import sqrt

class Circulo:
    def __init__(self, c, r):
        self.raio = r
        self.centro = c
        
    def distancia(self, p, outro):
        distancia = sqrt((outro.x - p.x)**2 + (outro.y - p.y)**2)
        return distancia
    
    def contem(self, ponto):
        if distancia(self.centro, ponto) > self.raio:
            return False
        else:
            return True
    