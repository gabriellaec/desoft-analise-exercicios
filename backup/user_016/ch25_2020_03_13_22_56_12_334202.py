import math
v = int(input('Qual a velocidade de lançamento? '))
a = int(input('Qual o ângulo de lançamento? '))
d = ((v**2)*(math.degrees(math.sin(2*a)))/9.8
if 98<d<102:
    print ('Acertou!')
elif d<=98:
    print ('Muito perto')
elif d>=102:
    print ('Muito longe')
