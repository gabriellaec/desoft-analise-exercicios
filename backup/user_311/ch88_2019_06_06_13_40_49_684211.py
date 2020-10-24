Class Retangulo():
    def __init__(self, x, y):
        self.base = abs(y.x - x.x)
        self.altura = abs(y.y - x.y)
    def calcula_perimetro(self, base, altura):
        self.perimetro = base*2 + altura*2
    def calcula_area(self, base, altura):
        self.area = base * altura / 2