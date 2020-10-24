class Circulo:
    def __init__(self, c, r):
        self.raio = r
        self.centro = c
    def contem(self, ponto):
        x = ponto.x
        if 0 >x:
            return True
        else:
            return False