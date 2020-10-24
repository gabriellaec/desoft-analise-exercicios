from math import sqrt
class Circulo():
    def __init__(self, ponto_centro, float_raio):
        self.x_centro = ponto_centro.x
        self.y_centro = ponto_centro.y
        self.raio = float_raio
    
    def contem(self,ponto):
        x_ponto = ponto.x
        y_ponto = ponto.y
        modulus = sqrt( (x_ponto - self.x_centro)**2 + (y_ponto - self.y_centro)**2 )
        if modulus > self.raio:
            return False
        else:
            return True