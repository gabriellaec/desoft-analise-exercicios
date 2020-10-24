[12:30, 11/27/2019] Gabriel Insper: class Retangulo:
    
    def _init_(self,p1,p2):
        self.p1x = p1.x
        self.p2x = p2.x
        self.p1y = p1.y
        self.p2y = p2.y
        
        
    def calcula_perimetro(self):
        
        ladoX = (self.p2x - self.p1x) * 2
        ladoY = (self.p2y - self.p1y) * 2
        perimetro = ladoX + ladoY 
        return perimetro
    
    def calcula_area(self):
        ladoX = (self.p2x - self.p1x)
        ladoY = (self.p2y - self.p1y)
        area = ladoX * ladoY
        return area