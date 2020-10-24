import math
class Circulo:
    def __init__(self,c,raio):
        self.cy=c.y
        self.cx=c.x
        self.raio=raio
    def contem(self,ponto):
        if (self.cx-ponto.x)**2+(self.cy-ponto.y)**2<=self.raio**2:
            return True
        else:
            return False