class Retangulo:
	def __init__(self,p1,p2):
		self.p1 = p1
		self.p2 = p2 

	def calcula_perimetro(self):
		a = p2.x - p1.x
		b = p2.y - p1.y
		return 2*(a+b)

	def calcula_area(self):
		a = p2.x - p1.x
		b = p2.y - p1.y
		return a*b
