class Retangulo:
    def __init__(self,p1,p2):
        self.b = p1.x - p2.x
        self.h = p1.y - p2.y
        
    def calcula_perimetro(self):
        self.p = 2*self.b + 2*self.h
    
        
    def calcula_area(self):
        self.a = self.b * self.h       