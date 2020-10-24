import math

v = float(input('Velocidade da Jaca:'))
o = float(input('Ângulo de lançamento:'))
a = o*(math.pi/180)
d = ((v**2)*math.sin(2*a))/9.8

if (d<98):
    print ('Muito perto')
elif (d>102):
    print ('Muito longe')
else:
    print ('Acertou!')