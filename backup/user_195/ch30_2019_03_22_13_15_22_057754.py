import math
velocidade=float(input("Qual a velocidade?"))
angulo=float(input("Qual a angulação"))
radianos=angulo*math.pi/180
g=9.8
d=velocidade**2*math.sin(2*radianos)/g
if d>102:
	print("Muito longe")
elif d<98:
	print("Muito perto")
else:
	print("Acertou!")