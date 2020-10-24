import math

class Circulo:
    def__init__(self, c, r):
        
        self.c = c
        self.r = r
        
        def contem(self, Ponto):
            if math.sqrt((Ponto.x-self.c.x)**2+(Ponto.y-self.c.y)**2) <= r:
                return True
            else:
                return False
        
        