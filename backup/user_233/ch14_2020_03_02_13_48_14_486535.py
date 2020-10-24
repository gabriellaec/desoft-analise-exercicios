from math import sqrt, sin, pi

def calcula_distancia_do_projetil(speed, angle, height):

	angle = angle * pi / 180

	return (speed ** 2) / 2 * 9.8 (1 + sqrt(1 + (2 * 9.8 * height) / ((speed ** 2) * sin(angle)) ** 2)) * sin(2 * angle)