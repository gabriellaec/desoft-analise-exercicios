class Retangulo:
    def __init__ (self, ie,sd):
        self.ie=ie
        self.sd=sd
        self.lado1=self.ie.y-self.sd.y
        self.lado2=self.sd.x-self.ie.x
    def calcula_perimetro(self):
        perimetro=2*self.lado1+2*self.lado2
        return perimetro
    def calcula_area(self):
        area=self.lado1*self.lado2
        return area
