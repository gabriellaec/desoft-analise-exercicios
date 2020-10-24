class Reatangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
        
    def perimetro(self):        
        perimetro = 2 * self.altura + 2* self.largura
        return perimetro
        
    def area(self):
        area = self.altura * self.largura
        return area
        