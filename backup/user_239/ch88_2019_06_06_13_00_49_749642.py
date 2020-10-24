class Retangulo():
    def __init__(self, Ie, Sd):
        self.base = Sd.x - Ie.x
        self.altura = Sd.y - Ie.y
    def calcula_perimetro(self):
        perimetro = self.base * 2 + self.altura * 2
        return perimetro
    def calcula_area(self):
        area = self.base * self.altura
        return area