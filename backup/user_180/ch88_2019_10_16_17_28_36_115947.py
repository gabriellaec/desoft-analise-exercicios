from math import sqrt

class Ponto:
    def __init__(self, x, y):
        self.x = xx
        self.y = y
    def distance_to(self, other_point):
        delta_x = self.x - other_point.x
        delta_y = self.y - other_point.y
        return sqrt(delta_x**2 + delta_y**2)


class Retangulo:
    def __init__(self, p1, p2):
        self.canto_inferior_esquerdo = p1
        self.canto_superior_direito = p2

    def calcula_perimetro(self):
        distanciax = abs(self.canto_superior_direito.x - self.canto_inferior_esquerdo.x)
        distanciay = abs(self.canto_superior_direito.y - self.canto_inferior_esquerdo.y)
        self.largura = distanciax
        self.altura = distanciay
        return distanciax*2 + distanciay*2
    
    def calcula_area(self):
        distanciax = abs(self.canto_superior_direito.x - self.canto_inferior_esquerdo.x)
        distanciay = abs(self.canto_superior_direito.y - self.canto_inferior_esquerdo.y)
        return distanciay * distanciax
        