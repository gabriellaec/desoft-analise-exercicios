import math
g=9.8

v = input('Digite a velocidade da jaca: ')
teta = input('Digite o angulo da jaca: ')

d = (v^2)*(math.sin(math.radians(teta)))/g

if d < 98:
    print('Muito perto')
    if d < 100:
        print('Acertou!')
elif d > 100:
    print('Muito longe')