class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    def dentro (self, ponto):
        if self.centro.distance_to(ponto) < self.raio:
            return True
        else:
            return False