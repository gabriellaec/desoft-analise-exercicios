class Retangulo:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        
    def calcula_perimetro(self, other_point):
        a = other_point.x - self.x
        b = other_point.y - self.y
        return 2*(a+b)
    
    def calcula_area(self, other_point):
        c = other_point.x - self.x
        d = other_point.y - self.y
        return c*d
