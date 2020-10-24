class Retangulo:
    def __init__(self,dx,dy):
        self.base = abs(self.dx1 + self.dx2)
		self.altura = abs(self.dy1 + self.dy2)
    def calcula_perimetro(self):
        self.perimetro = (2*(self.base+self.altura))
    	return self.perimetro
    def calcula_area(self):
        self.area = self.altura * self.base
        return self.area
