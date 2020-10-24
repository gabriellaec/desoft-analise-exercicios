from math import *
class Circulo:
    def __init__(self, O, r):
        self.O = O
        self.r = r
        
    def dista_do_centro(self, pt):
        a = sqrt((self.x - pt.x)**2 + (self.y - pt.y)**2)
        return a
    
    def contem(self, ponto):
        if self.O.dista_do_centro(ponto) < self.r:
            return True
        else:
            return False