import math
g=9.8

v = float(input('Digite a velocidade da jaca: '))
teta = float(input('Digite o angulo da jaca: '))

d = ((v**2)*(math.sin(math.radians(teta))))/g

if d > 98:
    if d < 100:
        print('Acertou!')
    else:
        print('Muito longe')
else:
     print('Muito perto')