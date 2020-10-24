class Retangulo():
    def __init__(self,P1,P2):
        self.P1x=P1.x
        self.P2x=P2.x
        self.P1y=P1.y
        self.P2y=P2.y
        ladoX=(self.P2x-self.P1x)
		ladoY=(self.P2y-self.P1y)
        
    def calcula_perimetro(self):
        ladoX=ladoX*2
        ladoY=ladoY*2
        Perimetro=ladoX+ladoY
        return Perimetro
    
    def calcula_area(self):
        ladoX=(self.P2x-self.P1x)
        ladoY=(self.P2y-self.P1y)
        Area=ladoX*ladoY
        return Area