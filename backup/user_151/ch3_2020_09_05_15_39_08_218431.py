import math
e = math.e
pi = math.pi

def calcula_gaussiana(x, y, z):
	resultado = (1 / (z * (2 * pi) * 1/2)) * (e * ((-1 / 2) * ((x - y) / z) ** 2))
	return resultado