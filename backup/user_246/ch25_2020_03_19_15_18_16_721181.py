import math
x=int(input("Angulo:"))
y=int(input("Velocidade:"))
d=((y**2)*math.sin(2*x))/9.8
if d>102:
    print('Muito longe')
elif d<98:
    print('Muito perto')
else:
    print('Acertou!')