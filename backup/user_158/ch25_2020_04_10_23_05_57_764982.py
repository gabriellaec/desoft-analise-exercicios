import math

v=int(input("velocidade de lancamento"))
a=int(input("angulo de lancamento"))

d=(v**2*math.sin(2*a))/9.8

if d == 100:
    print('Acertou!')
elif d < 100:
    print('Muito perto')
else:
    print('Muito longe')
