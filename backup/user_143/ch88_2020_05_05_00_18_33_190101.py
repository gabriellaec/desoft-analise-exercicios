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
p1=Ponto(7, 5)
p2=Ponto(5, 7)
2p=p1.calcula_perimetro(p2)
a=p1.calcula_area(p2)