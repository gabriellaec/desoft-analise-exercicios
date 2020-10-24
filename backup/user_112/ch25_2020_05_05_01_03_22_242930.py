import math

x = input('velocidade')
y = input('angulo')

v = float(x) ** 2
s = 2 * float(y)
a = math.sin(s)
d = v * a / 9.8

if d >= 98 and d <= 102:
    print('Acertou!')
elif d > 102:
    print('Muito longe')
else:
    print('Muito perto')
    

