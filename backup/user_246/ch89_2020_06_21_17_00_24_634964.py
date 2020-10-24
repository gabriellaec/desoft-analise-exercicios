class Circulo:
    def __init__(self, c, r):
        self.raio = r
        self.centro = c
    def contem(self, ponto):
        if (-self.raio) <= ponto.x <= self.raio and (-self.raio) <= ponto.y <= self.raio:
            return True
        else:
            return False