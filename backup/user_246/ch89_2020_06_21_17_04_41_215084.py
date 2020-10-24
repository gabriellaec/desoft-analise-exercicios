class Circulo:
    def __init__(self, c, r):
        self.raio = r
        self.centro = c
    def contem(self, ponto):
        if (self.centro - self.raio) <= Ponto.x <= (self.raio + self.centro) and (self.centro - self.raio) <= Ponto.y <= (self.raio + self.centro):
            return True
        else:
            return False