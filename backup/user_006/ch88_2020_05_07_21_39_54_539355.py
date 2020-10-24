class Retangulo:
    def __init__(self, p1, p2):
        self.ie= p1
        self.sd= p2
    def calcula_perimetro(self):
        a = self.p2.x -self.p1.x
        b = self.p2.y - self.p1.y
        per= 2*a+2*b
        return per
    def calcula_area(self):
        a = self.p2.x -self.p1.x
        b = self.p2.y - self.p1.y
        area=a*b
        return area