class Retangulo:
    def __init__(self, x1, x2, y1, y2):
        self.x  = x
        self.y  = y
        self.x1 = x1
        self.x2 = y2
        
    def calcula_perimetro(self):
        self.perimetro = 2*(self.x2-self.x1)+2*(self.y2-self.y1)
        
    def calcula_area(self):
        self.area = (self.x2-self.x1)*(self.y2-self.y1)