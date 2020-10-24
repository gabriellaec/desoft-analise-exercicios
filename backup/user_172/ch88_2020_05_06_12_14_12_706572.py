class Retangulo:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        
    def distance_to(self, other_point):
        dx = other_point.x - self.x
        dy = other_point.y - self.y
        
    def calcula_perimetro(self, dx, dy):
        p = dx*2 + dy*2
        return p
    
    def calcula_area(self, dx, dy):
        a = dx*dy