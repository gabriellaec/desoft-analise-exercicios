
class Retangulo:
    def __init__(self, ponto1, ponto2):
        self.ponto1 = ponto1
        self.ponto2 = ponto2
    def calcula_perimetro(self):
        self.perimetro = 2*((self.ponto2.x - self.ponto1.x) + (self.ponto2.y - self.ponto1.y))
    def calcula_area(self):
        self.area = ((self.ponto2.x - self.ponto1.x)*(self.ponto2.y - self.ponto1.y))
