class Circulo:
    def __init__(self, c, r):
        self.raio = r
        self.centrox = c[0]
        self.centroy = c[1]
    def contem(self, ponto):
        p = ponto.x
        r=self.raio
        c=self.centrox
        maxi = r+c
        mini = c - r
        if maxi > x and x > mini:
            return True
        else:
            return False