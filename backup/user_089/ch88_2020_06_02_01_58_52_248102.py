class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

ponto1 = Ponto(x,y)
ponto2 = Ponto(x,y)
class Retangulo:
    def __init__(self,ponto1,ponto2):
        self.ponto1 = ponto1.x,ponto1.y
        self.ponto2 = ponto2.x,ponto2.y
    def calcula_perimetro(self):
        self.perimetro = 2*(ponto2.x-ponto1.x)+2*(ponto2.y-ponto1.y)
    def calcula_area(self):
        self.area = (ponto2.x-ponto1.x)*(ponto2.y-ponto1.y)