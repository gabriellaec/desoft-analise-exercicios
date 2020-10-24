class Retangulo:    
    
    def __init__(self, ci, cs):
        self.ci = ci
        self.cs = cs        
    
    def calcula_perimetro(self):
        self.h = self.cs.y - self.cs.y
        self.l = self.cs.x - self.cs.x
        return 2*h+2*l
    
    def calcula_area(self):
        return self.h * self.l
        
        
        
        