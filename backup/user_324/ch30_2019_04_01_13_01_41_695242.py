import math
angulo=int(input('angulo: '))
v=int(input('velocidade: '))
d=(v**2)*math.sin(math.degrees(2*angulo))/9.8
if 98<=d<100 and 100<d<=102:
	print('Muito perto')
elif d==100:
	print('Acertou!')
else:
	print('Muito longe')
               