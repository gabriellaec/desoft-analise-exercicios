from math import *

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def entre_pontos(self, pt):
        return sqrt((self.x - pt.x)**2 + (self.y - pt.y)**2)


class Circulo:
    def __init__(self, O, r):
        self.O = O
        self.r = r
        
    
    
    def contem(self, ponto):
        a = self.O
        if a.entre_pontos(ponto) < self.r:
            return True
        else:
            return False