v = float(input('Qual a velocidade de lançamento? '))
a = float(input('Qual o ângulo de lançamento? '))
import math
d = ((v**2)*math.sin(2*math.radians(a)))/9.8
if d < 98:
    print('Muito perto')
elif d > 102:
    print('Muito longe')
else:
    print('Acertou!')