v = float(input('Qual a velocidade de lançamento? '))
angulo = float(input('Qual o ângulo de lançamento? '))
import math
d = (v**2*math.sin(2*angulo)/9.8)
if d < 98:
    print('Muito perto')
elif d > 102:
    print('Muito longe')
else:
    print('Acertou!')