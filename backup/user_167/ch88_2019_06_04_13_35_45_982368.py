class Retangulo :
    def __init__(self,ie,sd):
        self.altura= sd.y-ie.y
        self.base= sd.x-ie.x
    def  calcula_perimetro(self):
        p= 2*self.altura+ 2*self.base
        return p
    def calcula_area(self):
        a=self.base* self.altura
        return a
      
        