class Retangulo:
    def __init__ (self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    def calcula_perimetro (self):
        a = self.p1.x - self.p2.x
        b = self.p1.y - self.p2.y
        return 2*(a+b)
    def calcula_area (self):
        a = self.p1.x - self.p2.x
        b = self.p1.y - self.p2.y
        return a*b