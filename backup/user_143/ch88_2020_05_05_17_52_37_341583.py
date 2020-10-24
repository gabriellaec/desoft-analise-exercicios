class Retangulo:
    def __init__(self, p1, p2):
        self.p1 = x
        self.p1y = y
        self.p2 = x
        self.p2y = y
    def calcula_perimetro (self):
        dx= abs(self.p1 - self.p2)
        dy= abs(self.p1y -self.p2y)
        return (2 * dx + 2 * dy)
    def calcula_area (self):
        dx= abs(self.p1 - self.p2)
        dy= abs(self.p1y -self.p2y)
        return dx * dy
p1=Ponto(7, 5)
p2=Ponto(5, 7)
r=retangulo(p1, p2)
pp= r.calcula_perimetro()
a= r.calcula_area()
print(pp)
print(a)