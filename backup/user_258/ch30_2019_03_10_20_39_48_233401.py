v=int(input('Qual a velocidade do lançamento? '))
a=int(input('Qual o ângulo do lançamento? '))
import math
d=v**2*math.sin(2*a)/9.8
r=2
if d<100 and d+r<98:
    print('Muito perto')
elif d>100 and d-r>102:
    print('Muito longe')
else:
    print('Acertou!')
    