import math

class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    
    def distance_to(self, point):
        return sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
    
    def contem(self, ponto):
        if self.distance_to(ponto) < self.raio:
            return True
        else:
            return False