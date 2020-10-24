class Retangulo(object):
	def __init__(self,p1,p2):
		self.p1=p1
		self.p2=p2
	def calcula_perimetro(self):
		lado_menor=self.p2.y-self.p1.y
		lado_maior=self.p2.x-self.p1.x
		return 2*lado_menor+2*lado_maior
	def calcula_area(self):
		lado_menor=self.p1.y-self.p2.y
		lado_maior=self.p1.x-self.p2.x
		return lado_menor*lado_maior