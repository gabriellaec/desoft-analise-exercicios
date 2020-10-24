from math import sqrt
class Circulo:
    def __init__(self,center,radius):
        self.centro = center
        self.raio = radius
    def contem(self, Ponto):
        sqrt(self.x-ponto.x)**2+(self.y-ponto.y)
        if self.centro.distance_to(Ponto) < self.raio:
            return True
        else:
            return False
        