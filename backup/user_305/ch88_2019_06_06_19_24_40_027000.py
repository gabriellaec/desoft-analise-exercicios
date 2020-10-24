class Retangulo:
    def __init__(self, a, b):
        self.base = b.j - a.j
        self.altura = b.y - a.y
    
    def calcula_perimetro(self):
        perimetro = self.base * 2 + self.altura * 2
        return perimetro
    def calcula_area(self):
        area = self.base * self.altura
        return area
        
     
        