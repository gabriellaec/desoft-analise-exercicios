class Circulo:
    def __init__(self, c, r):
        self.raio = r
        self.centro = c
    def contem(self, ponto):
        x = ponto.x
        if self.raio >x:
            return True
        else:
            return False