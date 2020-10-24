class Retangulo:
    def __init__(self, SD, IE):
        self.base = SD.x - IE.x
        self.altura = SD.y - IE.y
    def calcula_perimetro(self):
        self.perimetro = self.base*2 + self.altura*2
       
    def calcula_area(self):
        self.area = self.base * self.altura

        