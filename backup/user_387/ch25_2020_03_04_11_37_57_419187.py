import math

t = float(input('t :'))

v = float(input('v :'))

d = ((v**2) * (math.sin(2*math.radians(t))))/9.8



if d > 98:
    print('Muito perto')

if d < 102:
    print('Muito longe')

else:
    print('Acertou!')