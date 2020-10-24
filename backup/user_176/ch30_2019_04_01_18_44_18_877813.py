import math
v= float(input('qual a velocidade? '))
p= float(input('qual o angulo? '))
g = 9.8
d= v**2*math.sin(math.radians(2*p))/g
if d<98:
    print('Muito perto')
elif d>102:
    print('Muito longe')
else:
    print('Acertou!')
