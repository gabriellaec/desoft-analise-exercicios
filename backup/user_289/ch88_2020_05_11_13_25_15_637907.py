class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Retangulo:
    p1 = Ponto(x, y)
    p2 = Ponto(z, w)
    def calcula_perimetro(self):
        dy = p1.y - p2.w
        dx = p1.x - p2.z
        return 2*dx + 2*dy
    def calcula_area(self):
        dy = p1.y - p2.w
        dx = p1.x - p2.z
        return dx*dy