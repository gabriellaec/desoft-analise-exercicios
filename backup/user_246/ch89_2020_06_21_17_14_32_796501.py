class Circulo:
    def __init__(self, c, r):
        self.raio = r
        self.centro = c
    def contem(self, ponto):
       
        if self.centro > ponto.x:
            return True
        else:
            return False