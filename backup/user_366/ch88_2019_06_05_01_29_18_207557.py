class Retangulo():
    
    def __init__(self, ponto1, ponto2):
        self.altura = ponto2.y - ponto1.y
        self.largura = ponto2.x - ponto1.x

    def calcula_perimetro(self):
            self.perimetro = 2*self.altura + 2*self.largura
            print(self.perimetro)

    def calcula_area(self):
            self.area = self.altura*self.largura
            print(self.area)