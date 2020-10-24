import math
def calcula_distancia (velocidade, angulo):
    angulo_radianos = math.degrees(angulo)
	distancia = ((velocidade**2) * math.sin(2*angulo_radianos))/9.8

	if distancia < 98:
		return 'Muito perto'
	elif distancia > 102:
		return 'Muito longe'
	else:
		return 'Acertou!'