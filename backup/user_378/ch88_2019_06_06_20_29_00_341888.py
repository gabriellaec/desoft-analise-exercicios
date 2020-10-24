class Retangulo():
    def __init__(self,P1,P2):
        self.P1x=P1.x
        self.P2x=P2.x
        self.P1y=P1.y
        self.P2y=P2.y
        self.ladoX=(self.P2x-self.P1x)*2
        self.ladoY=(self.P2y-self.P1y)*2
    def calcula_perimetro(self):
        Perimetro=ladoX+ladoY
        return Perimetro
    
    def calcula_area(self):
        Area=ladoX*ladoY
        return Area