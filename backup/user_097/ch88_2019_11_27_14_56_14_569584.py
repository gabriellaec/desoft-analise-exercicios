class Retangulo:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def calcula_perimetro(self):

        lado_1 = self.p2.x - self.p1.x
        lado_2 = self.p2.y - self.p1.y

        perimetro = abs((lado_1*2)+(lado_2*2))

        return perimetro

    def calcula_area(self):

        base = self.p2.x - self.p1.x
        altura = self.p2.y - self.p1.y

        area = abs(base*altura)

        return area