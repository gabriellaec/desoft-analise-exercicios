import math
def calcula_gaussiana(x, mi, sigma):
	resultado = (1 / (z * (2 * math.pi) * 1/2)) * (math.e ** ((-1 / 2) * ((x - mi) / sigma) ** 2))
	return resultado