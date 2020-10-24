class Circulo:
    def __init__(self, c, r):
        self.c = Ponto(x, y)
        self.r = r
    def contem(self, ponto):
        dist = ((ponto.x - self.c.x) ** 2 + (ponto.y - self.c.y) ** 2) ** 0.5
        if dist <= self.r:
            return True
        else:
            return False