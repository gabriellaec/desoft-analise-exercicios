class Ponto:
    def __init__(self, x, y):
        self.x= x
        self.y= y
class Circulo:
    def __init__(self, p, r):
        self.p= p
        self.r= r
    def contem(self, p):
        d1= (p.x - self.p.x) ** 2
        d2= (p.y - self.p.y) ** 2
        distancia = (d1 + d2)**(1/2)
        if distancia > self.r:
            return False
        return True