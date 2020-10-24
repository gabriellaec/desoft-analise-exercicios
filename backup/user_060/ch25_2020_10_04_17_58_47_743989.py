import math

v = float(input("velocidade escolhida"))
a = float(input("angulo escolhido"))
g = 9.8
d = ((v**2)*math.sin(2*a))/g

if d < 100:
    print('Muito perto')
elif d = 100:
    print('Acertou!')
else:
    print('Muito longe')
    