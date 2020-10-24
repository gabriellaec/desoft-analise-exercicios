class Retangulo():
    def __init__(self,Ponto1,Ponto2):
        self.largura = abs( Ponto2.x - Ponto1.x)
        self.altura = abs(Ponto1.y - Ponto2.y)

    def calcula_perimetro(self):
        Perimetro = (2*self.largura) + (2*self.altura)
        return Perimetro

    def calcula_area(self):
        Area = self.largura*self.altura
        return Area