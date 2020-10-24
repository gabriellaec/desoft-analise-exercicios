import math
g = 9.8

velocidade = float(input('Qual a velocidade? '))
θ = float(input('Qual o angulo? '))

distancia = ((velocidade**2) * (math.sin(math.radians(2*θ)))/g)

if distancia < 98:
	print ('Muito perto')
elif distancia > 102:
	print ('Muito longe')
else:
	print ('Acertou!')