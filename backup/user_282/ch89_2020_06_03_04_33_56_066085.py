from math import sqrt


class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance_to(self, ponto):
        return sqrt((self.x - ponto.x)**2 + (self.y - ponto.y)**2)


class Circulo:
    
    def __init__(self, c, r):
        self.centro = c
        self.raio = r
        
    def contem(self, ponto):
        if self.centro.distance_to(ponto) < self.raio:
            return True
        else:
            return False