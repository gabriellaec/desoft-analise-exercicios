class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
        
    def calcula_perimetro(self):        
        perimetro = 2 * self.altura + 2* self.largura
        return perimetro
        
    def calcula_area(self):
        area = self.altura * self.largura
        return area
        