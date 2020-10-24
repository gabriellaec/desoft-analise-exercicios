class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    def distance_to(self, other_point):
        return sqrt((self.x - other_point.x)**2 + (self.y - other_poit.y)**2)
    def contem (self, ponto):
        if self.centro.distance_to(ponto) < self.raio:
            return True
        else:
            return False