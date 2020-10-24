import math
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance_to(self,other_point):
        return math.sqrt((self.x-other_point.x)**2 + (self.y-other_point.y)**2)

class Circulo:
    def __init__(self,center,radius):
        self.centro = center
        self.raio = radius
        
    def contem(self, ponto):
        if self.centro.distance_to(ponto) < self.raio:
            return True
        else:
            return False