class Retangulo:
    def __init__(self,b,a):
		self.base = abs(self.b.x - self.a.x)
		self.altura = abs(self.a.y - self.b.y)
    def calcula_perimetro(self):
        self.perimetro = (2*(self.base+self.altura))
    	return self.perimetro
    def calcula_area(self):
        self.area = self.altura * self.base
        return self.area
