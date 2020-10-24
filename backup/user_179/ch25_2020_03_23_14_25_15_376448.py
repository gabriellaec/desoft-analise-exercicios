import math
def jacas (velocidade, angulo):
	g = 9.8
	distancia = ((velocidade**2) * math.sin(2*angulo))/g
	if distancia < 98:
		return 'Muito perto'
	elif distancia > 102:
		return 'Muito longe'
	else:
		return 'Acertou!'