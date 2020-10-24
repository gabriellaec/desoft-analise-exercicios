from math import sqrt

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