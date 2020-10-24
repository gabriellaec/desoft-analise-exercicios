import math
g = 9.8
vj = int(input("Diga a velocidade da jaca: "))
teta = int(input("Diga o ângulo de lançameto: "))
d = (vj**2)*(math.sin(2*teta))/g

if d<=98 and d>=102:
	print("Acertou!")
elif d<98:
	print("Muito perto")
else:
	print("Muito longe")