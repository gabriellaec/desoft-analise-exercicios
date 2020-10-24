from math import sqrt

class Ponto:
    def __init__ (self,vx,vy):
        self.x = vx
        self.y = vy

    def distance_to (self,other_point):
        d = sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return d

class Circulo(Ponto):
    def __init__ (self,centro,raio):
        self.c = centro
        self.r = raio
    
    def contem (self,ponto):
        if self.centro.distance_to(ponto) < self.r:
            return True
        else:
            return False