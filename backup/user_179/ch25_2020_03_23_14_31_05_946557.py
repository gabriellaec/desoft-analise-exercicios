import math
def calcula_distancia (velocidade, angulo):
    angulo_rad = math.degrees (angulo)
	g = 9.8
	distancia = ((velocidade**2) * math.sin(2*angulo_rad))/g
	if distancia < 98:
		return 'Muito perto'
	elif distancia > 102:
		return 'Muito longe'
	else:
		return 'Acertou!'