class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance_to(self, other_point):
        return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2) * (1/2)

class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    def contem (self, ponto):
        if self.centro.distance_to(ponto) < self.raio:
            return True
        else:
            return False

c = Point(5, 5)
R = 5
a = Point(4, 5)
b = Point(10, 2)
circ = Circulo(c, R)
print(circ.contem(a))
print(circ.contem(b))