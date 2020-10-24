class Retangulo:
    def __init__(self, ponto1, ponto2):
        self.p1 = ponto1
        self.p2 = ponto2
    def calcula_perimetro(self):
        h = self.p1.y - self.p2.y
        b = self.p1.x - self.p2.x
        per = 2*h + 2*b
        return per
    def calcula_area(self):
        h = self.p1.y - self.p2.y
        b = self.p1.x - self.p2.x
        area = h*b
        return area