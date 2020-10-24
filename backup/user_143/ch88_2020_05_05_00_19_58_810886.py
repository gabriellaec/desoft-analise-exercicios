class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def calcula_perimetro (self, other_point):
        dx= abs(other_point.x - self.x)
        dy= abs(other_point.y -self.y)
        return 2 * dx + 2 * dy
    def calcula_area (self, other_point):
        dx= abs(other_point.x - self.x)
        dy= abs(other_point.y -self.y)
        return dx * dy
p1=Retangulo(7, 5)
p2=Retangulo(5, 7)
pp=p1.calcula_perimetro(p2)
a=p1.calcula_area(p2)
print(pp)
print(a)