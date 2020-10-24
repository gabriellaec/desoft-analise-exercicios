from math import sqrt

class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    def contem(self, ponto):
        distancia_centro_ponto_x = abs(ponto.x - self.centro.x)
        distancia_centro_ponto_y = abs(ponto.y - self.centro.y)
        distancia_real = sqrt((distancia_centro_ponto_x**2) + (distancia_centro_ponto_y**2))
        if distancia_real <= self.raio:
            return True
        else:
            return False