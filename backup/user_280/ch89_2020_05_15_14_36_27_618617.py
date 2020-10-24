from math import sqrt

def distancia_para(self, outro_ponto):
    return sqrt((self.x - outro_ponto.x)**2 + (self.y - outro_ponto.y)**2)

class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    
    def contem(self, pinto):
        if self.centro.distancia_para(pinto) < self.raio:
            return True
        else:
            return False
        