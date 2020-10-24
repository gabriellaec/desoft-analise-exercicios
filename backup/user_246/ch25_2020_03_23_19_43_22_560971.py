import math
y=int(input("Velocidade:"))
x=int(input("Angulo:"))
x=math.degrees(x)
d=(y**2*math.sin(2*x))/9.8
if d>102:
    print('Muito longe')
elif d<98:
    print('Muito perto')
else:
    print('Acertou!')