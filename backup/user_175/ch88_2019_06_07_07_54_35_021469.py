class Retangulo():
	# essa é a classe retângulo que guarda informações. Para ser construída, ela requer 2 pontos(pontos 1 e 2):
	def __init__(self,ponto1, ponto2):	
		self.x1 = ponto1.x # ponto1 é do tipo Ponto (definido acima) e carrega consigo atributos x e y
		self.y1 = ponto1.y # analogamente ...

		self.x2 = ponto2.x # ... (ponto2 também é do tipo Ponto)
		self.y2 = ponto2.y # ...

		self.lado1 = abs(self.x1 - self.x2)  # o lado horizontal pode ser definido como a diferença (positiva) entre os valores "x" dos seus vértices
		self.lado2 = abs(self.y1 - self.y2)  # de forma análoga, o lado vertical é a diferença positiva entre os valores de y que os vertices assumem

	def calcula_perimetro(self):
		# os lados de um retângulo (com lados horizontais e verticais) podem ser definidos pelas diferenças entre as abscissas e as ordenadas de seus vértices:
		return 2*(self.lado1 + self.lado2)   # aparentemente, mesmo sem ser função, métodos também podem "retornar" valores

	def calcula_area(self):
		# de forma análoga, podemos resgatar valores (lados 1 e 2) definidos no método anterior e utilizar por aqui,
		# mas é preferível que definamos esses lados ainda no construtor
		area = self.lado1*self.lado2
		return area