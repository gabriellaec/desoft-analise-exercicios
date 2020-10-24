from math import sqrt
class Circulo:
    """Classe que representa um círculo"""
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio    
    def contem(self, ponto):
        distancia = sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        if distancia < self.raio:
            return True
        else:
            return False
        