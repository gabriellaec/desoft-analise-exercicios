class Retangulo:
    def __init__(self, other_point):
        dx = other_point.x - self.x
        dy = other_point.y - self.y
        
    def calcula_perimetro(self, dx, dy):
        p = dx*2 + dy*2
        return p
    
    def calcula_area(self, dx, dy):
        a = dx*dy
        return a