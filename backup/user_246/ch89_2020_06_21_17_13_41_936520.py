class Circulo:
    def __init__(self, c, r):
        self.raio = r
        self.centro = c
    def contem(self, ponto):
        x = Ponto.x
        if self.centro > x:
            return True
        else:
            return False