class Circulo:
    def __init__(self, p1, r):
        self.x = p1
        self.y = r
    def contem(self, ponto):
        if (((ponto.x - self.x.x)**2) + ((ponto.y - self.x.y)**2)) ** 0.5 < self.y:
            return True
        else:
            return False