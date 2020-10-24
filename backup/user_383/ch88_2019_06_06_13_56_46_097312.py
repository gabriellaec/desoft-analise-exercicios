class Retangulo:
    def __init__(self,ponto1,ponto2):
        self.base = self.ponto1.x - self.ponto2.x
        self.altura = self.ponto1.y - self.ponto2.y
    def calcula_perimetro(self):
        self.perimetro = 2*self.base + 2*self.altura
    	return self.perimetro
    def calcula_area(self):
        self.area = self.base*self.altura
        return self.area