import math

v = float(input())
a = float(input())
t = a*math.pi/180
g = 9.8
d = v**2*math.sin(2*t)/g
if d < 98:
    print('Muito perto')
elif d > 102:
    print('Muito longe')
else:
    print('Acertou!')
