class Retangulo:
    def _init_(self, P1, P2):
        self.P1=P1
        self.P2=P2
    def calcula_perimetro(self):
        perimetro = 2*(self.P2.x-self.P1.x)+2*(self.P2.y-self.P1.y)
        return perimetro
    def calcula_area(self):
        area = (self.P2.x-self.P1.x)*(self.P2.y-self.P1.y)
        return area