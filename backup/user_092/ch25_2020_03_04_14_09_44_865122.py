import math
v = float(input('qual a velocidade:'))
θ = float(input('qual os graus:'))
g = 9.8
a = math.radians(θ)
d = ((v**2)*(math.sin(2*a)))/g
if d>=102:
    print('Muito longe')
elif d<=98:
    print('Muito perto')
else:
    print('Acertou!')