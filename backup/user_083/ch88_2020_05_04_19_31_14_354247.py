class Retangulo:
    def __init__(self, p1, p2):
        self.pe = p1
        self.pd = p2
    def calcula_perimetro(self):
        a=self.pd.x-self.pe.x
        b=self.pd.y-self.pe.y
        return 2*(a+b)
    def calcula_area(self):
        a=self.pd.x-self.pe.x
        b=self.pd.y-self.pe.y
        return a*b
        