class Retangulo:
    def _init_(self, P1, P2):
        self.P1=P1
        self.P2=P2
    def calcula_perimetro(self):
        perimetro = 2*(P2.x-P1.x)+2*(P2.y-P1.y)
        return perimetro
    def calcula_area(self):
        area = (P2.x-P1.x)*(P2.y-P1.y)
        return area