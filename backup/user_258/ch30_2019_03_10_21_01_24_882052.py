import math
v=int(input('Qual a velocidade do lançamento? '))
a=int(input('Qual o ângulo do lançamento? '))
d=v**2*math.sin(2*a)/9.8
if d<96:
    print('Muito perto')
elif d>104:
    print('Muito longe')
else:
    print('Acertou!')
    