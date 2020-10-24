class Retangulo:
    def __init__(self,ponto1,ponto2):
        self.comprimento=ponto1.x-ponto2.x
        self.altura=ponto1.y-ponto2.y
        self.comprimento=(self.comprimento**2)**0.5
        self.altura=(self.altura**2)**0.5
    def calcula_perimetro(self):
        return  self.comprimento*2+self.altura*2
    def calcula_area(self):
        return  self.comprimento*self.altura