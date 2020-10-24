class Retangulo():
    def __init__(self, x, y):
        self.esq = x
        self.di = y
    def calcula_perimetro(self):
        return self.esq*2+self.di*2
    def calcula_area(self):
        return self.esq*self.di