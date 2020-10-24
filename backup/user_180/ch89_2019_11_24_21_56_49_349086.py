class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio

    def distance_to(self, other_pointx, other_pointy):
        delta_x = self.centro.x - other_pointx
        delta_y = self.centro.y - other_pointy
        return sqrt(delta_x ** 2 + delta_y ** 2)

    def contem(self, ponto):
        return self.centro.distance_to(Ponto.x, Ponto.y) <= self.raio