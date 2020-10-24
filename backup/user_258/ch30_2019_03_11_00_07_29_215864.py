import math
v=float(input('Qual a velocidade do lançamento? '))
a=float(input('Qual o ângulo do lançamento? '))
d=v**2*math.sin(math.radians(2*a))/9.8
if d<98:
    print('Muito perto')
    print (d)
elif d>102:
    print('Muito longe')
else:
    print('Acertou!')