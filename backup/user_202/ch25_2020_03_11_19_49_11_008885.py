import math
v = float(input('velocidade'))
a = float(input('angulo'))
a = a*math.pi/180
d = (v**2*math.sin(2*a))/9.8
if d >= 98 and d <= 102:
    print('Acertou!')
elif d < 98: 
    print('Muito perto')
else:
    print('Muito longe')