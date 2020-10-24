class Retangulo():
    
    def __init__(self, ponto1, ponto2):
        self.altura = ponto1.y - ponto2.y
        self.largura = ponto1.x - ponto2.x

    def calcula_perimetro(self):
            self.perimetro = 2*self.altura + 2*self.largura
            print(self.perimetro)

    def calcula_area(self):
            self.area = self.altura*self.largura
            print(self.area)