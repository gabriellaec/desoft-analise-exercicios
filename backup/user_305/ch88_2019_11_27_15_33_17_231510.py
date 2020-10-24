class Retangulo:
    def __init__(self, x, y):
        self.altura = x - x
        self.largura = y - y
        
    def calcula_perimetro(self):        
        perimetro = 2 * self.altura + 2* self.largura
        return perimetro
        
    def calcula_area(self):
        area = self.altura * self.largura
        return area
        