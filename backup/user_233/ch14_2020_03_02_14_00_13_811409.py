''' exercício 14 '''
from math import sqrt, sin, pi

def calcula_distancia_do_projetil(speed, angle, height):

	#angle = angle * pi / 180

	a = (speed ** 2) / (2 * 9.8)
	b = (2 * 9.8 * height) / ((speed * sin(angle)) ** 2)
	c = sin(2 * angle)

	return a * (1 + sqrt(1 + b)) * c