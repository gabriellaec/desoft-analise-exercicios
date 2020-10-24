class Retangulo():
    def __init__(self, x , y):
        self.P1x = P1.x
        self.P2y = P2.y
        self.P1y = P1.y
        self.P2x = P2.x
    def calcula_perimetro(self):
        lado_x = 2*(self.P2x - self.P1x)
        lado_y = 2*(self.P2y - self.P1x)
        2p = lado_x + lado_y
        return 2p
    def calcula_area(self):
        area = lado_x*lado_y/2
        return area