from math import *
vel = int(input("digite umaa velocidade:"))
teta = int(input("digite um angulo:"))
g=9.8
k= teta * pi/180
d = vel**2*sin(2*k)/g
if d<100:
    print('Muito perto')
elif d==100:
    print('Acertou!')
else:
    print('Muito longe')