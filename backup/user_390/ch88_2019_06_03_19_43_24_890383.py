class Retangulo:
    def __init__(self,Ie,Sd):
        self.altura=Sd.y-Ie.y
        self.base=Sd.x-Ie.x
    def calcula_perimetro(self):
        perimetro=2*self.altura + 2*self.base
        return perimetro
    def calcula_area(self):
        area=self.base*self.altura
        return area
        
        
        