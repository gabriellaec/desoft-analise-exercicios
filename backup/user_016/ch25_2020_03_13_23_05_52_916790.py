import math
v = float(input('Qual a velocidade de lançamento? '))
a = float(input('Qual o ângulo de lançamento? '))
d = ((v**2)*(math.degrees(math.sin(2*a))))/9.8
if 98<d<=100:
    print ('Acertou!')
elif d<=98:
    print ('Muito perto')
elif d>100:
    print ('Muito longe')
