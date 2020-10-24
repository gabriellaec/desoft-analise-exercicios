from math import sin

v = float(input('Digite a velocidade: '))
teta = float(input('Digite o ângulo: '))

d = (v**2 * sin(2 * teta)) / 9.8

if d < 96:
    print('Muito perto')
elif d > 104:
    print('Muito longe')
else:
    print('Acertou!')