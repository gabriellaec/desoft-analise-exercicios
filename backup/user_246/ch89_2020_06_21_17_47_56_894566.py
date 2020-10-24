class Circulo:
    def __init__(self):
        self.raio = 2
        self.centro = 0
    def contem(self, ponto):
        p = ponto.x
        r=self.raio
        c=self.centro
        maxi = r+c
        mini = c - r
        if maxi > x and x > mini:
            return True
        else:
            return False