class Retangulo:
    def _init_(self, P1x, P2x, P1y, P2y):
        self.P1x=P1.x
        self.P2x=P2.x
        self.P1y=P1.y
        self.P2y=P2.y
    def calcula_perimetro(self):
        perimetro = 2*(self.P2x-self.P1x)+2*(self.P2y-self.P1y)
        return perimetro
    def calcula_area(self):
        area = (self.P2x-self.P1x)*(self.P2y-self.P1y)
        return area