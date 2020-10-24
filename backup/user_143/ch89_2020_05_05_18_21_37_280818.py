class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class  Circulo:
    def __init__(self, p1, r):
        self.p1 = p1.x
        self.p1y = p1.y
        self.r = r
    def contem(self, ponto):
        xi = (self.p1 - ponto.x)**2
        yi= (self.p1y - ponto.y)**2
        d = 0.5**( xi + yi)
        if d<= self.r:
            return True
        else:
            return False
p1 = Ponto(7, 5)
p2 = Ponto(5, 7)
r = 2
c = Circulo(p1, r)
a = c.contem(p2)
print(a)
        