class Retangulo:
    def __init__(self, p1, p2):
        self.1 = p1
        self.2 = p2
    def calcula_perimetro(self):
        comp = self.2.x - self.1.x
        alt = self.2.y - self.1.y
        return 2 * (alt + comp)
    def calcula_area(self):
        comp = self.2.x - self.1.x
        alt = self.2.y - self.1.y
        return comp * alt