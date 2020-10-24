class Retangulo:
    def __init__(self,P1,P2):
        self.P1x = P1.x
        self.P1y = P1.y
        self.P2x = P2.x
        self.P2y = P2.y
    def calcula_perimetro(self):
        lado1 = (self.P2x - self.P1x)
        lado2 = (self.P2y - self.P1y)
        perimetro = 2*lado1 + 2* lado2
        return perimetro 
    def calcula_area(self):
        lado1 = (self.P2x - self.P1x)
        lado2 = (self.P2y - self.P1y)
        area = lado1*lado2
        return area
        
       
        
