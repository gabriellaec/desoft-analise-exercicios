y = int(input("Qual a distância que você irá percorrer? ")
	def preço(x):
		if (x<=200):
		return x*0.50
		else (x>200):
		return (200*0.50)+((x-200)*0.45)
print ("{0:.2f}".format(preço(y))