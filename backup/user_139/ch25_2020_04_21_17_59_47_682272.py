import math
g = 9.8
v = float (input('Qual a velocidade?')
y = float (input('Qual é o grau?')
d = (v ** 2 * (math.sin(2 * y))) / g
if d < 98:
    print ('Muito perto')
elif d > 102:
    print ('Muito longe')
else:
    print ('Acertou!')