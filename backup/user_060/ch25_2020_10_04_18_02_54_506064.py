import math

v = int(input("velocidade escolhida"))
a = int(input("angulo escolhido"))
g = 9.8
d = ((v**2)* math.sin(2*a)) / g

if d < 98:
    print('Muito perto')
elif d > 102:
    print('Muito longe)
else:
    print('Acertou!')
    