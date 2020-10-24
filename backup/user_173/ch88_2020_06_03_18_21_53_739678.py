class Retangulo:
    self.perimetro = perimetro
    self.area = area
    
    def calcula_perimetro(self):
        return 2*self.x + 2*self.y
    
    def calcula_area(self):
        return self.x * self.y