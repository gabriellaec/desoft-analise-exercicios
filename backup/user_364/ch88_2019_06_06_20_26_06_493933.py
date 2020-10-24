class Retangulo():
    def __init__(self,ie,sd):
        self.b= sd.x - ie.x
        self.h= sd.y - ie.y
     
    def calcula_perimetro(self):
        perimetro= 2*self.b + 2*self.h
        return perimetro
    
    def calcula_area(self):
        area= self.b* self.h
        return area
    
    