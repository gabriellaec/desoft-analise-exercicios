import math
g = 9.8

velocidade = int(input('Qual a velocidade? '))
angulo = int(input('Qual o angulo? '))

def calcula_distancia (velocidade, angulo):
    angulo_radianos = math.degrees(angulo)
	distancia = ((velocidade**2 * math.sin(2*angulo_radianos))/g)
	return distancia

if distancia < 98:
	print ('Muito perto')
elif distancia > 102:
	print ('Muito longe')
else:
	print ('Acertou!')