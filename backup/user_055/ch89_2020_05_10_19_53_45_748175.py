from math import sqrt
from math import pi
class Circulo:
    def __init__(self, o, r):
        self.o = o
        self.r = r

    def contem(self, ponto):
        dOP = sqrt((self.o.x - ponto.x)**2 + (self.o.y - ponto.y)**2)
        if dOP < self.r:
            return True
        else:
            return False