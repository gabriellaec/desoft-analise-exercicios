import math 
velocidade=int(input('Qual a velocidade da sua jaca? '))
angulo=int(input('Qual é o ângulo de lançamento da sua catapulta? '))
g=9.8
d=(velocidade**2*math.sin(2*angulo))/g
if d<98:
	print('Muito perto')
if d>102:
	print('Muito longe')
else:
	print('Acertou!')