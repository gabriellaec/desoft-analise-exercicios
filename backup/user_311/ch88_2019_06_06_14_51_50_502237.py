class Retangulo():
    def __init__(self, x, y):
        self.base = abs(y.x - x.x)
        self.altura = abs(y.y - x.y)
    def calcula_perimetro(self):
        self.perimetro = (self.base + self.altura)*2
        return self.perimetro
    def calcula_area(self):
        self.area = self.base * self.altura 
        return self.area