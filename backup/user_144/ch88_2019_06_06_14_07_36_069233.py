class Retangulo:
    def __init__(self,P1,P2):
        self.x1 = P1.x
        self.y1 = P1.y
        self.x2 = P2.x
        self.y2 = P2.y
        
    def calcula_perimetro(self):
        ladoX = 2*abs(self.x1 - self.x2)
        ladoY = 2*abs(self.y1 - self.y2)
        perimetro = ladoX + ladoY
        return perimetro
    
    def calcula_area(self):
        ladoX = abs(self.x1 - self.x2)
        ladoY = abs(self.y1 - self.y2)
        area = ladoX * ladoY
        return area
    
        
        
       
        