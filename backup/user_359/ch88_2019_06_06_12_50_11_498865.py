class Retangulo:
    def __init__(self, x, y):
        self.bottomleft = x
        self.topright = y
    def calcula_perimetro(self):
        self.perimetro = self.bottomleft*2 + self.topright*2
    def calcula_area(self):
        self.area = self.bottomleft * self.topright
        