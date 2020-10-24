class Retangulo:
    def __init__(self,p1,p2):
        self.pe = p1
        self.pd = p2
    
    def calculo_perimetro(self):
        x = self.pe.x - self.pd.x
        y = self.pe.y - self.pd.y
        return y*2+x*2
    
    def calcula_area(self):
        x = self.pe.x - self.pd.x
        y = self.pe.y - self.pd.y
        return y*x