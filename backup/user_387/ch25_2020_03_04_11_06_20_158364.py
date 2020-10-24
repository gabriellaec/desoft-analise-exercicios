import math

t = 30
v = 5
d = (v**2 * math.sin(2*t))/9.8

d = 5

if d > 0 and d <= 2:
    print('Muito perto')

if d > 2:
    print('Muito longe')

if d == 0:
    print('Acertou!')