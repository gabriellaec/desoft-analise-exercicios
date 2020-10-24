import math

class Retangulo:
    def __init__(self, p1, p2):
        self.a1 = p1
        self.a2 = p2
    
    def calcula_perimetro(self):
        l1 = self.a1.x - self.a2.x
        l2 = self.a1.y - self.a2.y
        return math.fabs(2*l1 + 2*l2)

    def calcula_area(self):
        l1 = self.a1.x - self.a2.x
        l2 = self.a1.y - self.a2.y
        return l1*l2