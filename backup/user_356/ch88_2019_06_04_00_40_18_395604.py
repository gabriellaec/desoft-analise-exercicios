class Retangulo():
    def __init__(self, x, y):
        self.esq = x
        self.di = y
    def calcula_perimetro(self):
        return Ponto.x*2+Ponto.y*2
    def calcula_area(self):
        return Ponto.x*Ponto.y