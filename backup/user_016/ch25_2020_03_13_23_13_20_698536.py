import math
v = float(input('Qual a velocidade de lançamento? '))
a = float(input('Qual o ângulo de lançamento? '))
d = ((v**2)*(math.pi)*(math.sin(2a)))/9.8
if 98<d<102:
    print ('Acertou!')
elif d<=98:
    print ('Muito perto')
elif d>100:
    print ('Muito longe')
