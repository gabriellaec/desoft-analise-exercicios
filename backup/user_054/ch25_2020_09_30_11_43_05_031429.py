import math
v = int(input('qual a velocidade? '))
a = int(input('qual o angulo? '))
g = 9.8

d = int (v*v * math.sin(2*a)/g)
if d < 100:
    print('Muito perto')
elif d > 100:
    print ('Muito longe')
else:
    print('Acertou!')