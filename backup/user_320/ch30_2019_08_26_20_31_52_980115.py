from math import sin

v = int(input('Digite a velocidade: '))
teta = int(input('Digite o ângulo: '))

d = (v**2 * sin(2 * teta)) / 9.8

if d < 102:
    print('Muito perto')
elif d > 98:
    print('Muito longe')
else:
    print('Acertou!')