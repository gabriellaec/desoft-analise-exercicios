import math
v = int(input('Escolha uma velocidade inicial: ')
o = int(input('Escolha um ângulo de lançamento: ')

g = 9.8
d = ((v ** 2) * math.sin(math.radians(o) * 2))/ g

if d < 98:
   print('Muito perto!')
elif d > 102:
   print('Muito longe')
else:
   print('Acertou!')