class Retangulo:
    def __init__(self, x, y):
        self.x = Ponto(x)
        self.y = Ponto(y)
    def calcula_perimetro(self, other_point):
        dx= abs(other_point.x - self.x)
        dy= abs(other_point.y -self.y)
        return (2 * dx + 2 * dy)
    def calcula_area(self, other_point):
        dx= abs(other_point.x - self.x)
        dy= abs(other_point.y -self.y)
        return (dx*dy)
        
        