class Retangulo:
    def __init__(self,Ie,Sd):
        self.altura=Sd.y-Ie.y
        self.base=Sd.x-Ie.x
    def calcula_perimetro(self):
        perimetro=2*altura + 2*base
        return perimetro
    def calcula_area(self):
        area=base*altura
        return area
        
        
        