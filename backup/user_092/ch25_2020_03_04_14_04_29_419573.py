import math
g = 9.8
v = float(input('qual a velocidade'))
θ = float(input('qual os graus'))
a = math.radians(θ)
d = ((v**2)*(math.sin(2*a)))/g
if d>=102:
    print('Muito longe')
elif d<=98:
    print('Muito perto')
elif d<102 and d>98:
    print('Acertou!')