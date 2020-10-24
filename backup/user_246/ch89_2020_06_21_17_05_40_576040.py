class Circulo:
    def __init__(self, c, r):
        self.raio = r
        self.centro = c
    def contem(self, ponto):
        if (self.raio - self.centro) <= ponto.x <= (self.raio + self.centro) and (self.raio - self.centro) <= ponto.y <= (self.raio + self.centro):
            return True
        else:
            return False