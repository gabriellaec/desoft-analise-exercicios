class Circulo:
    def __init__(self, c, r):
        self.raio = r
        self.centro = c
    def contem(self, ponto):
        x = ponto.x
        r=self.raio
        c=self.centro
        maxi = r+c
        mini = c - r
        if maxi > x and x > mini:
            return True
        else:
            return False