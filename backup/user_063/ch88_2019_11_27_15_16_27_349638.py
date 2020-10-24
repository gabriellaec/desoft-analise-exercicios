class Retangulo:
    def _init_(self,p1,p2):
        self.canto1x = p1.x
        self.canto1y = p1.y
        self.canto2x = p2.x
        self.canto2y = p2.y
        self.width = abs(p1.x-p2.x)
        self.lenght = abs(p1.y-p2.y)
           
    def calcula_perimetro(self):
        perimetro = 2*(self.width + self.lenght)
        return perimetro
             
    def calcula_area(self):
