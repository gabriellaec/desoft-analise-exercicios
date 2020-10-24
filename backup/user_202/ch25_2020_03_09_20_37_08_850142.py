import math
v = int(input('velocidade'))
a = int(input('angulo'))
a = 2*a*math.pi/360
d = (v**2*math.sin(2*a))/9.8
if d > 98 and d < 102:
    print('Acertou!')
elif d <= 98: 
    print('Muito perto')
else:
    print('Muito longe')