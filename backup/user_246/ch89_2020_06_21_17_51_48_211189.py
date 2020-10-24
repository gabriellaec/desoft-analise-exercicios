class Circulo:
    def __init__(self, c, r):
        self.raio = r
        self.centrox = c.x
        self.centroy = c.y
    def contem(self, ponto):
        x = ponto.x
        r=self.raio
        c=self.centrox
        maxi = r+c
        mini = c - r
        if maxi > x and x > mini:
            return True
        else:
            return False