class Retangulo:
    def __init__ (self, p1, p2):
        self.pe = p1
        self.pd = p2
        
    def calcula_perimetro(self):
        base = self.pe.x -self.pd.x
        h = self.pe.y - self.pd.y
        perimetro = (base+h)*2
        return perimetro
    
    def calcula_area(self):
        base = self.pe.x -self.pd.x
        h = self.pe.y - self.pd.y
        area = base*h
        return area