class Ponto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
class Retangulo:        
    def calcula_perimetro(self):
        return 2*self.x + 2*self.y
    
    def calcula_area(self):
        return self.x * self.y