from math import sqrt
class Point:
    """Classe que representa um ponto."""
    def __init__(self, a, b):
        self.x = a
        self.y = b
    def distante_to(self, other_point):
        """Calcula a distância entre o próprio ponto e outro ponto."""
        return sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
          
class Retangulo:
    """Classe que representa um retângulo."""
    def __init__(self, p1, p2):
        self.pie = p1
        self.psd = p2  
    def calcula_perimetro(self):
        dy = self.psd.y - self.pie.y
        dx = self.psd.x - self.pie.x
        return 2*(dy + dx)
    def calcula_area(self):
        dy = self.psd.y - self.pie.y
        dx = self.psd.x - self.pie.x
        return dx*dy
    
    