class Retangulo:
    def __init__(self, e, d):
        self.lado1 = abs(e.x - d.x) 
        self.lado2 = abs(e.y - d.y)
    def calcula_perimetro(self):
        self.P = self.lado1*2 + self.lado2*2
        return self.P
    def calcula_area(self):
        self.a = self.lado1*self.lado2
        return self.a        
    