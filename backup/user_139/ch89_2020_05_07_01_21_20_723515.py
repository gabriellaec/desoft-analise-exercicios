from math import sqrt
class Point:
    def __init__(self, vx, vy):
        self.x = vx
        self.y = vy
    def distancia(self, other_point):
        return sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    def contem(self, ponto):
        if self.centro.distancia(ponto) < self.raio:
            return True
        else:
            return False