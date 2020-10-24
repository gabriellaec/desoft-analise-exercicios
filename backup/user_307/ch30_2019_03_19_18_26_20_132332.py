#d>98 and d<102


import math

v=float(input("qual a velocidade? "))
teta=float(input("Quantos graus? "))
g=9.8

d=((v**2)*math.sin(2*teta))/g
print(d)

if d>98 and d<102:
	print('Acertou!')
elif d>90 and d<110:
	print ('Muito perto')
else:
	print ('Muito longe')