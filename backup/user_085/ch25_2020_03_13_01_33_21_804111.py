import math
v = float(input('Digite a velocidade de lançamento da jaca: '))
a = float(input('Digite aqui o ângulo de lançamento da jaca: '))
g = 9.8
d = ((v**2) * math.sin(2*a))/g
if d>102:
    print('Muito longe')
elif d<98:
    print('Muito perto')
else:
    print('Acertou!')