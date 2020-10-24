#d>98 and d<102


import math

v=float(input("qual a velocidade? "))
teta=float(input("Quantos graus? "))
g=9.8
rad=teta*math.pi/180


d=((v**2)*math.sin(2*rad))/g
print(d)

if d>=98 and d<=102:
	print('Acertou!')
elif d<98:
	print ('Muito perto')
else:
	print ('Muito longe')