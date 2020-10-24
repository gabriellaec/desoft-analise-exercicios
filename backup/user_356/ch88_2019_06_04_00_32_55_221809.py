class Retangulo():
    def __init__(Ponto):
        self.esq = Ponto.x
        self.dir = Ponto.y
    def calcula_perimetro(self):
        return self.esq*2+self.dir*2
    def calcula_area(self):
        return self.esq*self.dir