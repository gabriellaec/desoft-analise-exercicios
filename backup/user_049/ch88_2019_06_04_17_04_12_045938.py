class Retangulo:  
    def __init__(self, P1, P2):
        self.P1x = P1.x
        self.P2x = P2.x
        self.P1y = P1.y
        self.P2y = P2.y
        
    def calcula_perimetro(self):
        ladoX = (P1x - P2x) * 2
        ladoY = (P1y - P2y) * 2
        perimetro = ladoX + ladoY
        return perimetro
    
    def calcula_area(self):
        ladoX = (P1x - P2x)
        ladoY = (P1y - P2y)
        area = ladoX * ladoY
        return area
    