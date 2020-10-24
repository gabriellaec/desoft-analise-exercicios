from math import sin, radians

v = float(input('Digite a velocidade: '))
teta = float(input('Digite o ângulo: '))
teta = radians(teta)

d = (v**2 * sin(2 * teta)) / 9.8
print(d)
if d < 98:
    print('Muito perto')
elif d > 102:
    print('Muito longe')
else:
    print('Acertou!')