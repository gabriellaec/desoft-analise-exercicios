class Circulo:
    def __init__(self, c, r):
        self.raio = r
        self.centro = c
    def contem(self, ponto):
        if 0 <= ponto.x <= (self.raio*2-self.centro) and 0 <= ponto.y <= (self.raio*2-self.centro):
            return True
        else:
            return False