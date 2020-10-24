import math

g = 9.8

vj = int(input("Diga a velocidade da jaca: "))

teta = int(input("Diga o ângulo de lançameto: "))

d = (vj**2)*(math.sin(2*teta))/g

if d<98:
	print('Muito perto')
elif d>102:
	print('Muito longe')
else:
	print('Acertou!')