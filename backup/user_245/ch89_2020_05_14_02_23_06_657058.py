from math import sqrt
class Circulo:
    def __init__(self,center,radius):
        self.centro = center
        self.raio = radius
    def contem(self, ponto):
        if (self.centro.x - self.raio.x) < self.raio:
            return True
        else:
            return False
        