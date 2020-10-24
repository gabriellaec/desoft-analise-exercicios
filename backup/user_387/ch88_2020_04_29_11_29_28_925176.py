class Retangulo:    
    
    def __init__(self, ci, cs):
        self.ci = ci
        self.cs = cs        
    
    def calcula_perimetro(self):
        self.h = self.cs.y - self.cs.y
        self.l = self.cs.x - self.cs.x
        return 2*self.h+2*self.l
    
    def calcula_area(self):
        return self.h * self.l
        
        
        
        