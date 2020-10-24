import math
g = 9.8

velocidade = float(input('Qual a velocidade? '))
angulo = float(input('Qual o angulo? '))

def calcula_distancia (velocidade, angulo):
    angulo_radianos = math.radians(angulo)
	distancia = (velocidade**2 * math.sin(2*angulo_radianos))/g
	return distancia

if distancia < 98:
	print ('Muito perto')
elif distancia > 102:
	print ('Muito longe')
else:
	print ('Acertou!')