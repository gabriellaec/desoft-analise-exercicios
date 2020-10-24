import math
v=int(input("velocidade:"))
a=int(input("angulo:"))
f=((v**2)*math.sin(2*a)/(9.8))
	if f<98:
       	print('Muito perto')
	elif f>=98 and f<=102:
       	print('Acertou!')
	else:
       	print('Muito longe')