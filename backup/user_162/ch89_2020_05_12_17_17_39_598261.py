
from math import *

class Circulo:
    def __init__(self, x, y, O, r):
        self.O = O
        self.r = r
        self.x = x
        self.y = y
        
    def entre_pontos(self, pt):
        return sqrt((self.x - pt.x)**2 + (self.y - pt.y)**2)
    
    def contem(self, ponto):
        a = self.O
        if a.entre_pontos(ponto) < self.r:
            return True
        else:
            return False