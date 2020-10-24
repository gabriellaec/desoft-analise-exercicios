class Retangulo:
    def __init__(self, P1, P2):
        self.P1X=P1.x
        self.P2X=P2.x
        self.P1Y=P1.y
        self.P2Y=P2.y
    
    def calcula_perimetro(self):
        ladosX = abs(self.P1X-self.P2X) *2
        ladosY = abs(self.P1Y-self.P2Y)* 2
        perimetro = ladosX + ladosY
        return perimetro
    def calcula_area(self):
        ladoX = abs(self.P1X-self.P2X)
        ladoY = abs(self.P1Y-self.P2Y)
        area = ladoX*ladoY
        return area
    