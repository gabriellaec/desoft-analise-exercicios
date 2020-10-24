import math
g=9.8

v = float(input('Digite a velocidade da jaca: '))
teta = float(input('Digite o angulo da jaca: '))

d = ((v**2)*(math.sin(math.radians(2*teta))))/g

if d < 98:
    print('Muito perto')
else:
    if d < 102:
        print('Acertou!')
    else:
        print('Muito longe')