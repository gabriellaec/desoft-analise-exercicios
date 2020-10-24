import math
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
            
    def distance_to(self, point):
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
    
class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    
    def contem(self, ponto):
        if self.centro.distance_to(ponto) < self.raio:
            return True
        else:
            return False