class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self, c, r):
        self.c = Ponto()
        self.r = r
    def contem(self, ponto):
        self.ponto = Ponto(x, y)
        dist = ((ponto.x - c.x) ** 2 + (ponto.y - c.y) ** 2) ** 0.5
        if dist <= r:
            True
        else:
            False