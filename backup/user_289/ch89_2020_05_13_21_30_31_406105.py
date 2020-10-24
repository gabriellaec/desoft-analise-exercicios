from math import sqrt
class Circulo:
    """Classe que representa um círculo"""
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio    
    def contem(self, ponto):
        distancia = sqrt((self.centro.x - ponto.x)**2 + (self.centro.y - ponto.y)**2)
        if distancia < self.raio:
            return True
        else:
            return False
        