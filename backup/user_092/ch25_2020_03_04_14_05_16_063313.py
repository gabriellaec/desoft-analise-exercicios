import math
g = 9.8
v = int(input('qual a velocidade'))
θ = int(input('qual os graus'))
a = math.radians(θ)
d = ((v**2)*(math.sin(2*a)))/g
if d>=102:
    print('Muito longe')
elif d<=98:
    print('Muito perto')
else:
    print('Acertou!')