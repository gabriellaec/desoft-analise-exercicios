class Retangulo:
    
    def __init__(self, ponto1, ponto2):
        self.ponto1 = ponto1
        self.ponto2 = ponto2
        self.altura = abs(self.ponto1.y - self.ponto2.y)
        self.largura = abs(self.ponto1.x - self.ponto2.x)
        
    def calcula_perimetro(self):
        return self.altura * 2 + self.largura * 2
    
    def calcula_area(self):
        return self.altura * self.largura
        