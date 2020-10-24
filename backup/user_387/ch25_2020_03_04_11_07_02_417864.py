import math

t = int()
v = int()
d = (v**2 * math.sin(2*t))/9.8

if d > 0 and d <= 2:
    print('Muito perto')

if d > 2:
    print('Muito longe')

if d == 0:
    print('Acertou!')