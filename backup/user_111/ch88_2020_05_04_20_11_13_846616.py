class Retangulo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
       
    def calcula_perimetro(self):
        perimetro=2*self.x+2*self.y
        return perimetro
        
    def calcula_area(self):
        area = self.x*self.y
        return area