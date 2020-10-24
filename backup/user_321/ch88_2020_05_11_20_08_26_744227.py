class Retangulo:
    def __init__ (self, Ponto1, Ponto2):
        self.pe = Ponto1
        self.pd = Ponto2
        
    def calcula_perimetro(self):
        dp = (((pe.x - pd.x)**2) + ((pe.y - pd.y)**2)) ** 0.5
        perimetro = ((dp**2)*2)**0.5
        return perimetro
    
    def calcula_area(self):
        base = pe.x -pd.x
        h = pe.y - pd.y
        area = base*h
        return area