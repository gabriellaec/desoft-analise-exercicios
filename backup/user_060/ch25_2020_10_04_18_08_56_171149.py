import math

v = int(input("velocidade escolhida: "))
teta = int(input("angulo escolhido: "))

d = ((v**2) * math.sin(2*teta))/9.8

if d < 98:
    print('Muito perto')
elif d > 102:
    print('Muito longe')
elif 98 < d < 102
    print('Acertou!')
    