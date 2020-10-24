import math
velocidade=int(input("Qual a velocidade?")
angulo=int(input("Qual a angulação")
g=9.8
d=velocidade**2*math.sin(angulo*2)/g
if d>102:
	print("Muito perto")
elif d<98:
	print("Muito longe")
else:
	print("Acertou")