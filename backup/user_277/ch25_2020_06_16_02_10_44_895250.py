from math import *
vel = float(input("digite umaa velocidade:"))
teta = float(input("digite um angulo:"))
g=9.8
k= teta * pi/180
d = vel**2*sin(2*k)/g
if d<98:
    print('Muito perto')
elif d>=98 and d<=102:
    print('Acertou!')
else:
    print('Muito longe')