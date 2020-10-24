class Retangulo:
    def __init__ (self,a,b):
        self.x1 = a.x
        self.x2 = b.x
        self.y1 = a.y
        self.y2 = b.y
    def calcula_perimetro (self):
        dx = abs(self.x1 - self.x2)
        dy = abs(self.y1 - self.y2)
        perimetro = 2*(dx + dy)
        return perimetro
    def calcula_area (self):
        dx = abs(self.x1 - self.x2)
        dy = abs(self.y1 - self.y2)
        area = dx * dy
        return area