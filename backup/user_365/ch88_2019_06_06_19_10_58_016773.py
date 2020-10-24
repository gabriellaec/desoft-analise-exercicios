class Retangulo:
    def __init__(self,P1,P2):
        self.P1x=P1.x
        self.P2x=P2.x
        self.P1y=P1.y
        self.P2y=P2.y
    def calcula_perimetro(self):
        ladox=(self.P2x-self.P1x)*2
        ladoy=(self.P2y-self.P1y)*2
        per=ladox+ladoy
        return perimetro
    def calcula_area(self):
        ladox=(self.P2x-self.P1x)
        ladoy=(self.P2y-self.P1y)
        area=ladox*ladoy
        return area
    