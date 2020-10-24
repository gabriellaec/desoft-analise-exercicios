class Retangulo:
    def __init__(self,P1,P2):
        self.P1x=P1.x
        self.P1y=P1.y
        self.P2x=P2.x
        self.P2y=P2.y
    def calcula_perimetro(self):
        ladoX=(self.P2x-self.P1x)*2
        ladoY=(self.P2y-self.P1y)*2
        perimetro=ladoy+ladox
        return perimetro
    def area(self):
        ladoX=(self.P2x-self.P1x)*2
        ladoY=(self.P2y-self.P1y)*2
        area=ladoy*ladox
        return area