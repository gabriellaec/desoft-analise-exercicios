class Retangulo(self):
    def __init__(p1,p2):
        self.p1 = self.Ponto.x
        self.p2 = self.Ponto.y 
    def calcula_perimetro(self):
        self.perimetro = self.p1 + self.p1 + self.p2 + self.p2
    def calcula_area (self):
        self.area = self.p1 * self.p2
        