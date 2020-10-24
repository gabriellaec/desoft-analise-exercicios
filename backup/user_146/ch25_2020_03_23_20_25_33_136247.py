import math
g = 9.8
v = float(input('Velocidade? '))
a = float(input('Angulo? '))
rad=(math.pi/180)*a
d=((v**2)*math.sin(2*rad))/g
if (d<=102 and d>=98):
    print('Acertou!')
elif 102<d:
    print('Muito longe')
else:
    print('Muito perto')