class Retangulo:
    def __init__(self, SD, IE):
        self.base = abs(SD.x - IE.x)
        self.altura = abs(SD.y - IE.y)
    def calcula_perimetro(self):
        self.perimetro = self.base*2 + self.altura*2
        return self.perimetro
    def calcula_area(self):
        self.area = self.base * self.altura
        return sel.area

        