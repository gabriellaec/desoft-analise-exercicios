class Retangulo:
    def __init__(self, Ponto1, Ponto2):
        self.ponto1 = Ponto1
        self.ponto2 = Ponto2
    def calcula_perimetro(self):
        perimetro = (self.ponto2.x - self.ponto1.x)*2 + (self.ponto2.y - self.ponto1.y)*2
        
    def calcula_area(self):
        area = (self.ponto2.x - self.ponto1.x)*(self.ponto2.y - self.ponto1.y)