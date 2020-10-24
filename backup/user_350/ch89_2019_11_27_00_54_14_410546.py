from math import sqrt 
class Circulo:
    def __init__(self,p,r):
        self.centro = p
        self.raio = r
    def contem(self, other_point):
        return sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2) <= self.raio