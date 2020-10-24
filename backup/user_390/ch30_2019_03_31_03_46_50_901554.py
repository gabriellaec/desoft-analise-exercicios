import math
v=float(input('velocidade'))
a=float(input('angulo'))
g=9.8
d=((v**2)*math.sin(2*a))/g
if d>101.9:
    print('Muito longe')
elif d<98.1:
    print('Muito perto')
else:
    print('Acertou')