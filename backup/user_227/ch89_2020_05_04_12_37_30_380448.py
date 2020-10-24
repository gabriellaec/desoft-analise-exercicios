from math import sqrt
class Circulo:
    def __init__(self, centro, raio):
        self.c=centro
        self.r=raio
    
    def contem(self, ponto):
        if self.centro.distance_to(ponto) < self.raio:
            return True
        else:
            return False