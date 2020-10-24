class Retangulo:
    def __init__(self, p1, p2):
        self.x = x
        self.y = y
    def calcula_perimetro (self):
        dx= abs(p1 - p2)
        dy= abs(p1 -self.y)
        return 2 * dx + 2 * dy
    def calcula_area (self, other_point):
        dx= abs(other_point.x - self.x)
        dy= abs(other_point.y -self.y)
        return dx * dy
p1=Ponto(7, 5)
p2=Ponto(5, 7)
r=retangulo(p1, p2)
pp= r.calcula_perimetro()
a= r.calcula_area()
print(pp)
print(a)