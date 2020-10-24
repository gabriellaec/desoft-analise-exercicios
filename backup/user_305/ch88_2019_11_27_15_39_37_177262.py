class Retangulo:
    def __init__(self, p1, p2):
        self.largura = abs(p1.x - p2.x)
        self.altura = abs(p1.y - p2.y)
        
    def calcula_perimetro(self):        
        perimetro = 2 * self.altura + 2* self.largura
        return perimetro
        
    def calcula_area(self):
        area = self.altura * self.largura
        return area
        