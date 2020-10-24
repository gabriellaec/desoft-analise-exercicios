import math
v = int(input('Qual a velocidade de lançamento? '))
a = int(input('Qual o ângulo de lançamento? '))
f = math.radians(a)
h = math.sin(2*f)
d = ((v**2)*(math.degrees(h))/9.8
if 98<d<102:
    print ('Acertou!')
elif d<=98:
    print ('Muito perto')
else:
    print ('Muito longe')
