class Retangulo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def calcula_perimetro(self,x,y):
        return x + x + y + y
    
    def calcula_area(self,x,y):
        return x*y