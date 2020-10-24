import math

def calcula_norma(vetor):
	quadrado = 0
	for i in vetor:
		quadrado += i**2
	norma = math.sqrt(quadrado)
	return norma