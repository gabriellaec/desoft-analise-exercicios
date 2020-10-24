import math

v = float(input("velocidade escolhida"))
a = float(input("angulo escolhido"))

d = ((v**2) * math.sin(2*a))/9.8

if d < 98:
    print('Muito perto')
elif d > 102:
    print('Muito longe')
else:
    print('Acertou!')
    