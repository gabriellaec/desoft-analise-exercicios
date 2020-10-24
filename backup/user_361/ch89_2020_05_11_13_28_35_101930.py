class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    
    def distance_to(self, other_point):
        return ((self.centro.x - other_point.x)**2 + (self.centro.y - other_point.y)**2) * (1/2)
    
    def contem (self, ponto):
        return self.distance_to(ponto) <= self.raio