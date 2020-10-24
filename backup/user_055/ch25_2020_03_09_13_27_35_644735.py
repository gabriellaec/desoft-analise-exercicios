import math
v = float(input('Velocidade: '))
θ = int(input('Ângulo: '))
l = ((v**2)*(math.sin(math.radians(2*θ))))/9.8
if l > 98 and l < 102:
    print('Acertou!')
if l > 102:
    print('Muito longe')
if l < 98:
    print('Muito perto')

