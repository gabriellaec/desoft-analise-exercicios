class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def calcula_perimetro(self, other_point):
        dx = other_point - self.x
        dy = other_point - self.y
        return 2*(dx+dy)
    def calcula_area(self, other_point):
        dx = other_point - self.x
        dy = other_point - self.y
        return dx*dy
