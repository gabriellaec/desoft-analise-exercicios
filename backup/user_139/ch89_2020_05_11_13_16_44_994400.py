class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    def distance_to(other_point):
        return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2) * (1/2)
    def contem (self, ponto):
        if distance_to(ponto) < self.raio:
            return True
        else:
            return False