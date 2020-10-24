import math
v = input('Qual a velocidade de lançamento? ')
a = input('Qual o ângulo de lançamento? ')
d = ((v**2)*math.sin(2*a))/9.8
if 98<d<102:
    print ('Acertou')
elif d<=98:
    print ('Muito perto')
else:
    print ('Muito longe')
