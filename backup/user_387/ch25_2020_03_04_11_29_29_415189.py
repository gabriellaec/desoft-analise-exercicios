import math

t = float(input('t :'))

v = float(input('v :'))

d = ((v**2) * (math.sin(math.rad(2*t))))/9.8



if d > 0 and d <= 98:
    print('Muito perto')

if d > 98:
    print('Muito longe')

if d == 0:
    print('Acertou!')