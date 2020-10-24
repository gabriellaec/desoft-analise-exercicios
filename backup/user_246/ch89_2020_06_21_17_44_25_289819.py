class Circulo:
    def __init__(self, c, r):
        self.raio = r
        self.centro = c
    def contem(self, ponto):
        p = ponto(x,y)
        r=self.raio
        c=self.centro
        maxi = r+c
        mini = c - r
        if maxi > p.x and p.x > mini:
            return True
        else:
            return False