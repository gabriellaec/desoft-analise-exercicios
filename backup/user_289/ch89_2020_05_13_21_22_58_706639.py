from math import sqrt
class Ponto:
    """Classe que representa um ponto"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance_to(self, other_point):
        return sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
class Circulo:
    """Classe que representa um círculo"""
    def __init__(self, centro, raio):
        self.c = centro
        self.r = raio
    def contem(self, ponto):
        d = sel.centro.distance_to(ponto)
        if d < self.r:
            return True
        else:
            return False
        