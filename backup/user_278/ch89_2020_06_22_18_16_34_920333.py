from math import sqrt

class Circulo:
    def __init__ (self,centro,raio):
        self.c = centro
        self.r = raio
    
    def contem (self,ponto):
        dx = (self.c.x - ponto.x)**2
        dy = (self.c.y - ponto.y)**2
        d = sqrt (dx + dy)
        if d < self.r:
            return True
        else:
            return False