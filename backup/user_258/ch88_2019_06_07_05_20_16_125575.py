class Retangulo(object):
    def __init__(self, P1, P2):
        self.P1x = P1.x
        self.P2x = P2.x
        self.P1y = P1.y
        self.P2y = P2.y
    
    def calcula_perimetro(self):
        ladoX = (self.P2x - self.P1x) * 2
        ladoY = (self.P2y - self.P1y) * 2
        perimetro = ladoX + ladoY
        return perimetro
    
    def calcula_area(self):
        ladoX = (self.P2x - self.P1x) 
        ladoY = (self.P2y - self.P1y) 
        area = ladoX * ladoY
        return area
        