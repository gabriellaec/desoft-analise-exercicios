import math
v = int(input('Escolha uma velocidade inicial: '))
a = int(input('Escolha um ângulo de lançamento: '))

g = 9.8
d = ((v ** 2) * math.sin(math.radians(2 * a)))/ g

if d < 100:
    print('Muito perto')
elif d > 100:
    print('Muito longe')
else:
    print('Acertou!')