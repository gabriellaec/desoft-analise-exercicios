import math
def distance_to(self, other_point):
    return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    def contem(self, point):
        if self.centro.distance_to(point) < self.raio:
            return True
        else:
            return False
        
    