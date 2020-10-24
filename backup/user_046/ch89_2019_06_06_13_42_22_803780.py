class Circulo:
	def __init__(self,ponto1,raio):
		self.x=ponto1.x
		self.y=ponto1.y
		self.Raio=raio
	def contem(self,ponto):
		if (self.x-ponto.x)**2+(self.y-ponto.y)**2>raio**2:
			return True
		else:
        	return False