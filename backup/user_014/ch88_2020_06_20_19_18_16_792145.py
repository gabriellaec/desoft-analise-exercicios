from math import sqrt

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance_to(self, other_point):
        return sqrt((self.x - other_point.x)**2 + (self.y - other_poit.y)**2)
    
class Retangulo:
    def __init__(self, p1, p2):
        self.ponto_inferior = p1
        self.ponto_superior = p2
    def calcula_perimetro(self):
        a = self.ponto_superior.x - self.ponto_inferior.x
        b = self.ponto_superior.y - self.ponto_inferior.y
        return 2 * (a+b)
    
    def calcula_area(self):
        a = self.ponto_superior.x - self.ponto_inferior.x
        b = self.ponto_superior.y - self.ponto_inferior.y
        return a * b