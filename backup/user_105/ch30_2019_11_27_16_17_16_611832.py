import math 
velocidade=float(input('Qual a velocidade da sua jaca? '))
angulo=float(input('Qual é o ângulo de lançamento da sua catapulta? '))
g=9.8
d=(velocidade**2*math.sin(2*angulo*math.pi/180))/g
if d<98:
	print('Muito perto')
elif d>102:
	print('Muito longe')
else:
	print('Acertou!')