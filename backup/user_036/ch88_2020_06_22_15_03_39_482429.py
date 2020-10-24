class Retangulo:
    def __init__(self, x1, y1, x2, y2):
        self.ponto1 = Ponto(x1, y1)
        self.ponto2 = Ponto(x2, y2)
    def calcula_perimetro(self):
        (self.ponto1.x1-self.ponto2.x2)*2 + (self.ponto1.y1-self.ponto2.y2)*2
    def calcula_area(self):
        (self.ponto1.x1-self.ponto2.x2)*(self.ponto1.y1-self.ponto2.y2)