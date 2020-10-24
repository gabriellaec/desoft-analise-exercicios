class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class  Circulo:
    def __init__(self, p1, r):
        self.p1 = p1.x
        self.p1y = p1.y
    def contem(self, ponto):
        xi = (self.p1 - ponto.x)**2
        print(xi)
        yi= (self.p1y - ponto.y)**2
        print(yi)
        d = ( xi + yi)
        e = d**0.5
        print(e)
        print(d)
        print(r)
        if e<= r:
            return True
        else:
            return False
p1 = Ponto(7, 5)
p2 = Ponto(80, 90)
r = 0.2
c = Circulo(p1, r)
a = c.contem(p2)
print(a)
        