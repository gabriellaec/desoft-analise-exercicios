import math

v = int(input('Velocidade da Jaca:'))
o = int(input('Ângulo de lançamento:'))
d = ((v**2)*math.sin(2*o))/9.8

if (d<=98):
    print ('Muito perto')
elif (d>=102):
    print ('Muito longe')
else:
    print ('Acertou!')