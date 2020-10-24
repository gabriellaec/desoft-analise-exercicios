from math import sqrt

class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    def contem(self, ponto):
        distancia_centro_ponto_x = abs(self.centro.x - ponto.x)
        distancia_centro_ponto_y = abs(self.centro.y -ponto.y)
        distancia_real = sqrt((distancia_centro_ponto_x**2) + (distancia_centro_ponto_y**2))
        if distancia_real <= self.raio:
            print("O ponto está contido no círculo")
        else:
            print("O ponto não está contido no círculo")