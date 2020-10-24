from math import sqrt
def distance_to(self, other_point):
    return sqrt((self.x - other_point.x)**2+(self.y - other_point.y)**2)
class Circulo:
    def __init__(self, centro, raio):
        self.centro=centro
        self.raio=raio
    def contem(self, ponto):
        if self.centro.distance_to(ponto)<self.raio:
            return True
        else:
            return False
                
    
        