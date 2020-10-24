class Circulo:
	def __init__(self,centro,raio):
		self.centro = centro 
		self.raio = raio

	def contem(self,ponto):
		dist = sqrt((self.centro.x - ponto.x)**2 + (self.centro.y - ponto.y))
		if dist > self.raio:
			return False
		else:
			return True