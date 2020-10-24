class Retangulo:
    def __init__(self,p1,p2):
        self.pd = p1
        self.pe = p2
    
    def calcula_perimetro(self):
        base = self.pe.x - self.pd.x
        h = self.pe.y - self.pd.y
        return base*2+h*2
    
    def calcula_area(self):
        base = self.pe.x - self.pd.x
        h = self.pe.y - self.pd.y
        return base*h