class Circulo:
	def __init__(self, centro, raio):
		self.centro = centro
		self.raio   = float(raio)
	def contem(self, ponto):
		distPontoRaio = ((ponto.x**2)+(ponto.y**2))**0.5
		if distPontoRaio > self.raio:
			return False
		else:
			return True