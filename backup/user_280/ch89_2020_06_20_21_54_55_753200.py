import math

def distancia_para(self, outro_ponto):
    return sqrt((self.x - outro_ponto.x)**2 + (self.y - outro_ponto.y)**2)

class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    
    def contem(self, ponto):
        if math.sqrt((self.centro.x - ponto.x)**2 + (self.centro.y - ponto.y)**2) < self.raio:
            return True
        else:
            return False
        