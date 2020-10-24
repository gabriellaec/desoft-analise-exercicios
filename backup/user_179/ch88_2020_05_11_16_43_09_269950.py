class Retangulo:
    def __init__ (self, x1_coord, y1_coord, x2_coord, y2_coord):
        self.x1 = x1_coord
        self.y1 = y1_coord
        self.x2 = x2_coord
        self.y2 = y2_coord
    def calcula_perimetro(self):
        return (self.x2 - self.x1)*2 + (self.y2 - self.y1)*2
    def calcula_area(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1)