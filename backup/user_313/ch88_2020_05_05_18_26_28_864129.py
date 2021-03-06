class ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to(self, other_point):
    """ Calcula a distância entre o próprio ponto e o outro ponto."""
        return sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

class Retangulo:
    
    def __init__(self, p1, p2):
        self.x = p1
        self.y = p2
        
    def calcula_perimetro(self):
        a = self.y.x - self.x.x
        b = self.y.y - self.x.y
        return 2 * (a + b)
    
    def area(self):
        a = self.y.x - self.x.x
        b = self.y.y - self.x.y
        
        return a * b