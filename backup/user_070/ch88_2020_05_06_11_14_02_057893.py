class Retangulo:
    def __init__(self, p1, p2):
        self.x = p1
        self.y = p2
    def calcula_perimetro(self):
        comp = self.y.x - self.x.x
        alt = self.y.y - self.x.y
        return 2 * (comp + alt)
    def calcula_area(self):
        return comp * alt