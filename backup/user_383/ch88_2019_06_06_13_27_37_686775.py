class Retangulo:
    def __init__(self,dx,dy):
		self.base = abs(self.dx1.x - self.dx2.x)
		self.altura = abs(self.dy1.y - self.dy2.y)
    def calcula_perimetro(self):
        self.perimetro = (2*(self.base+self.altura))
    	return self.perimetro
    def calcula_area(self):
        self.area = self.altura * self.base
        return self.area
