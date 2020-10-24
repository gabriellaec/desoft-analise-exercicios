class Retangulo:
    def __init__(self,ponto1,ponto2):
        self.comprimento= ponto2.x - ponto1.x
        self.altura = ponto2.y - ponto1.y
        self.p1 = ponto1
        self.p2 = ponto2    
    def calcula_perimetro(self):
        perimetro = self.altura*2 + self.comprimento*2
        return perimetro
    def calcula_area(self):
        area = self.altura*self.comprimento
        return area
