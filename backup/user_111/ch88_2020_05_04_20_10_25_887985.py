class Retangulo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
       
    def calcula_perimetro(self,x,y):
        perimetro=2*x+2*y
        return perimetro
        
    def calcula_area(self,x,y):
        area = x*y
        return area