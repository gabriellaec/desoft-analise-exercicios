from math import sqrt 
class Circulo:
    def __init__(self,p,r):
        self.centro = p
        self.raio = r
    def contem(self, ponto):
        return sqrt((self.x - ponto.x)**2 + (self.y - ponto.y)**2) <= r