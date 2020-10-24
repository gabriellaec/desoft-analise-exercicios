class Retangulo:
    def __init__(self, p1, p2):
        self.a = p1
        self.b = p2
    def calcula_perimetro(self):
        comp = self.b.x - self.a.x
        alt = self.b.y - self.a.y
        return 2 * (comp + alt)
    def calcula_area(self):
        comp = self.b.x - self.a.x
        alt = self.b.y - self.a.y
        return comp * alt