class Retangulo:
    def __init__(self, p1, p2):
        self.ie = p1
        self.sd = p2
    def calcula_perimetro(self):
        a = self.sd.y - self.ie.y
        b = self.sd.x - self.ie.x
        return (2*a + 2*b)
    def calcula_area(self):
        a = self.sd.y - self.ie.y
        b = self.sd.x - self.ie.x
        return b*a