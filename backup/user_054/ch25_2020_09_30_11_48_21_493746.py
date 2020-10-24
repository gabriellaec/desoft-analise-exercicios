import math
v = int(input('qual a velocidade? '))
a = math.radians(int(input('qual o angulo? ')))
g = 9.8

d = (v* v * math.sin(2*a)/g)
if d < 98:
    print('Muito perto')
elif d > 102:
    print ('Muito longe')
else:
    print('Acertou!')