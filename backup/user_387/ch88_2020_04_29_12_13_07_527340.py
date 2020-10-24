class Retangulo:
    def __init__(self, ci, cs):
        self.ci = ci
        self.cs = cs        
        self.h = self.cs.y - self.ci.y
        self.l = self.cs.x - self.ci.x

    def calcula_perimetro(self):                
        return 2*self.h+2*self.l

    def calcula_area(self):
        return self.h*self.l
        
        
        
        