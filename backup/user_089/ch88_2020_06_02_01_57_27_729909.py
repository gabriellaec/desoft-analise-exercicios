ponto1 = Ponto()
ponto2 = Ponto()
class Retangulo:
    def __init__(self,ponto1,ponto2):
        self.ponto1 = ponto1.x,ponto1.y
        self.ponto2 = ponto2.x,ponto2.y
    def calcula_perimetro(self):
        self.perimetro = 2*(ponto2.x-ponto1.x)+2*(ponto2.y-ponto1.y)
    def calcula_area(self):
        self.area = (ponto2.x-ponto1.x)*(ponto2.y-ponto1.y)