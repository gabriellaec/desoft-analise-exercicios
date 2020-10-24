import math
v = float(input('Digite a velocidade do projetil: '))
a = math.degrees(float(input('Digite o angulo de lancamento: ')))
g = 9.8
d = ((v**2) * math.sin(a*2))/g
if d<98:
    print('Muito perto')
elif 98<d<102:
    print('Acertou!')
else:
    print('Muito longe')