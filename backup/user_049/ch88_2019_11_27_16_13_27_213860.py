class Retangulo:
    def _init_(self,p1,p2):
        self.b = (p2.x - p1.x)
        self.h = (p2.y - p1.y)
        
    def calcula_perimetro(self):
        self.p = 2*self.b + 2*self.h
        return self.p
    
        
    def calcula_area(self):
        self.a = self.b * self.h     
        return self.a