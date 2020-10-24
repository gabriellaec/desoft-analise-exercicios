class Retangulo():
    def __init__(self, x, y):
        self.esq = Ponto.x
        self.di = Ponto.y
    def calcula_perimetro(self):
        return self.esq*2+self.di*2
    def calcula_area(self):
        return self.esq*self.di