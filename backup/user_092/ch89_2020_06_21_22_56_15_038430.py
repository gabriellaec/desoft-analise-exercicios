import math
class Retangulo:
    ra = 0.0
    def __init__(self,p1,ra):
        self.p = p1
        self.r = ra
    def contem(self,ponto):
        self.p2 = ponto
        self.p + self.r > self.p2 