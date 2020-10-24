class Retangulo:
    def __init__ (self, p1, p2):
        self.pe = p1
        self.pd = p2
        
    def calcula_perimetro(self):
        dp = (((self.pe-self.pd)**2) + ((self.pe - self.pd)**2)) ** 0.5
        perimetro = ((dp**2)*2)**0.5
        return perimetro
    
    def calcula_area(self):
        base = self.pe -self.pd
        h = self.pe - self.pd
        area = base*h
        return area