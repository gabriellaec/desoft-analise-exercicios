class Circulo:
    def __init__(self, c, r):
        self.c = c
        self.r = r
    def contem(self, ponto):
        self.ponto = ponto(x, y)
        dist = ((ponto.x - self.c.x) ** 2 + (ponto.y - self.c.y) ** 2) ** 0.5
        if dist <= r:
            return True
        else:
            return False