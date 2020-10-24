import math
v = float(input('Qual a velocidade da jaca? '))
a = float(input('Qual o angulo de lancamento da jaca? '))

d = ((v**2)*math.sin(2*a))/9.8

if 98 < d < 102:
    print('Acertou!')
elif d <= 98:
    print('Muito perto')
elif d >= 102:
    print('Muito longe')



