from math import sqrt
class Circulo:
    def __init__(self, centro, raio):
        self.c=centro
        self.r=raio
    
    def contem(self, ponto):
        distancia=sqrt((self.c.x-ponto.x)**2+(self.c.y-ponto.y)**2)
        
        if distancia<=self.r:
            return True
        else:
            return False