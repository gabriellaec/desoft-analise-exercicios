import math
a = int(input('Velocidade:   '))
b = int(input('Ângulo em graus:   '))
d = (v**2)/9.8*math.sin(2*b)
if d < 98:
    print('Muito perto')
elif d > 102:
    print('Muito longe')
else:
    print('Acertou!')