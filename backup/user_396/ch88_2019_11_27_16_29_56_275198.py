class Retangulo():
	def _init_(self,p1,p2):
		self.inferior = p1
		self.superior = p2
	def calcula_area(self):
		return (self.superior.x - self.inferior.x)*(self.superior.y - self.inferior.y)
	def calcula_perimetro(self):
		return (2*(self.superior.x - self.inferior.x))+(2*(self.superior.y - self.inferior.y))

