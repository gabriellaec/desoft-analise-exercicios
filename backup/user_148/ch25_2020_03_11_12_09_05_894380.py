import math
v = float(input('Qual a velocidade do laçamento? '))
a = float(input('Qual o ângulo de lançamento? '))
a = math.radians(a)
d = ((v**2)*math.sin(2*a))/9.8
if d<100:
    print('Muito perto')
elif d==100:
    print('Acertou!')
elif d>100:
    print('Muito longe')