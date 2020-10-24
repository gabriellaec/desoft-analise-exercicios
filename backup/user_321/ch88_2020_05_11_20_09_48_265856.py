class Retangulo:
    def __init__ (self, Ponto1, Ponto2):
        self.pe = Ponto1
        self.pd = Ponto2
        
    def calcula_perimetro(self):
        dp = (((self.pe-self.pd)**2) + ((self.pe - self.pd)**2)) ** 0.5
        perimetro = ((dp**2)*2)**0.5
        return perimetro
    
    def calcula_area(self):
        base = self.pe -self.pd
        h = self.pe - self.pd
        area = base*h
        return area