class Retangulo:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        
    def calcula_perimetro(self):
        a = self.x
        b = self.y
        return 2*(a+b)
    
    def calcula_area(self):
        c = self.x
        d = self.y
        return c*d
