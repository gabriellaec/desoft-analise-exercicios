import math

class Circulo():
    def __init__(self, c, r):
        
        self.c = c
        self.r = r
        
    def contem(self, ponto):
        if math.sqrt((ponto.x-self.c.x)**2+(ponto.y-self.c.y)**2) <= self.r:
            return True
        else:
         	return False
        
        