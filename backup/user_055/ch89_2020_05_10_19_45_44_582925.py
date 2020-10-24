from math import sqrt
from math import pi
class Circulo:
    def __init__(self, o, r):
        self.o = o
        self.r = r

    def contem(self, ponto):
        dOP = sqrt((self.o.x - self.ponto.x)**2 + (self.o.y - self.ponto.y)**2)
        area = pi * (self.r**2)
        if dOP <= area:
            return True
        else:
            return False