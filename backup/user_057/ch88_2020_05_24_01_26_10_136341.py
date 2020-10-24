class Retangulo:
    def __init__(self, p1, p2):
        self.Ie = p1
        self.Sd = p2

    def calcula_perimetro(self):
        perimetro = 2 * ((self.Ie).x - (self.Sd).x) + 2 * ((self.Ie).y - (self.Sd))
        return perimetro

    def calcula_area(self):
        area = ((self.Ie).x - (self.Sd).x)*((self.Ie).y - (self.Sd))
        