import math
def d(v,θ):
    y=((v**2)*math.sin(2*θ))/9.8
    return y
a=input('Velocidade')
b=input('Ângulo')
a=float(a)
b=float(b)
c = math.radians(b)
z=float(d(a,c))
if z<98:
	print('Muito perto')
elif z<=102 and z>=98:
	print('Acertou!')
elif z>102:
	print('Muito longe')