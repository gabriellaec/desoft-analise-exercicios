class Retangulo:
    def __init__(self,ponto1,ponto2):
        self.p1x = ponto1.x
        self.p1y = ponto1.y
        self.p2x = ponto2.x
        self.p2y = ponto2.y
    def calcula_perimetro(self):
        perimetro = 2*(self.p2x-self.p1x) + 2*(self.p2y-self.p1y)
        return perimetro
    def calcula_area(self):
        area = (self.p2x-self.p1x)*(self.p2y-self.p1y)
        return area