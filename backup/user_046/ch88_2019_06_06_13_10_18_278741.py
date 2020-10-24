class Retangulo:
	def __init__(self,sd,ie):
		self.base=abs(sd.x-ie.x)
		self.altura=abs(sd.y-ie.y)
	def calcula_perimetro(self):
		self.perimetro=self.base*2+self.altura*2
		return self.perimetro
	def calcula_area(self):
		self.area=self.base*self.altura
		return self.area