from math import sqrt
class Circulo:
    def __init__(self,center,radius):
        self.centro = center
        self.raio = radius
    def distance_to(self, outro):
        return sqrt(self.x-outro.x)**2+(self.y-outro.y)
    def contem(self, Ponto):
        if self.centro.distance_to(Ponto) < self.raio:
            return True
        else:
            return False
        