class Retangulo:
    def __init__(self, ponto1, ponto2):
        self.x1 = ponto1.x
        self.y1 = ponto1.y
        self.x2 = ponto2.x
        self.y2 = ponto2.y
    def distanciax_y(self):
        dx = abs(self.x1-self.x2)
        dy = abs(self.y1 - self.y2)
        return dx, dy
    def calcula_perimetro(self):
        return 2*dx + 2*dy
    def calcula_area(self):
        area = dx*dy
        return area