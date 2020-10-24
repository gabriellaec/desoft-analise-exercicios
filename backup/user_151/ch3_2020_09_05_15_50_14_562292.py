import math
def calcula_gaussiana(x, y, z):
	resultado = (1 / (z * (2 * math.pi) * 1/2)) * (math.e ** ((-1 / 2) * ((x - y) / z) ** 2))
	return resultado