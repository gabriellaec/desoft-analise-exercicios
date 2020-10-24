import math

v = float(input('Qual a velocidade do laçamento? '))
a = float(input('Qual o ângulo de lançamento? '))
ar = math.radians(2*a)
g = 9.8
d = ((v**2)*math.sin(ar))/g

if d<98:
    print('Muito perto')
elif 98<=d<=102:
    print('Acertou!')
elif d>102:
    print('Muito longe')
    