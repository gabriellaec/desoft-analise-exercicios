import math
v = float(input('Escolha uma velocidade inicial: '))
a = float(input('Escolha um ângulo de lançamento: '))

g = 9.8
d = ((v ** 2) * math.sin(2 * math.radians(a)))/ g

if d >= 98 or d <= 102 :
    print('Acertou!')
elif d < 98:
    print('Muito perto')
else:
    print('Muito longe')