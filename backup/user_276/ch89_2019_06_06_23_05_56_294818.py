class Circulo:
    def __init__(self, x, y, raio):
		self.x = x
		self.y = y
		self.raio = raio
        def contem(self, ponto):
		if Ponto.x - Circulo.x > Circulo.raio and Ponto.y - Circulo.y > Circulo.raio:
			print("Fora do círculo")
		elif Ponto.x - Circulo.x < Circulo.raio and Ponto.y - Circulo.y < Circulo.raio:
			print("Dentro do círculo")