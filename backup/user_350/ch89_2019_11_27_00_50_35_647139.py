from math import sqrt 
class Circulo:
    def __init__(self,pc,r):
        self.centro = pc
        self.raio = r
    def contem(self, ponto):
        if sqrt((self.centro.x - self.ponto.x)**2 + (self.centro.y - self.ponto.y)*2) <= self.raio:
            return True
        else:
            return False