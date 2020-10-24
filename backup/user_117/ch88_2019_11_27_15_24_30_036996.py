class Retangulo:
    def __init__(self,p1,p2):
        self.b = p2.x - p1.x
        self.h = p2.y - p1.y
        base = self.b
        altura = self.h
        
    def calcula_perimetro(self):
        self.p = 2 * base + 2 * altura
    
        
    def calcula_area(self):
        self.a = base * altura
        return a
        