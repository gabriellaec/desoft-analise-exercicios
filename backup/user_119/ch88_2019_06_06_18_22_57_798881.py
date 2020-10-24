class Retangulo():
    def __init__(self, P1, P2):
        self.P1x = P1.x
        self.P2x = P2.x
        self.P1y = P1.y
        self.P2y = P2.y
    def calcula_perimetro(self):
        lado_x = 2*(self.P2x - self.P1x)
        lado_y = 2*(self.P2y - self.P1y)
        p = lado_x + lado_y
        return p
    def calcula_area(self):
        area = lado_x*lado_y/2
        return area