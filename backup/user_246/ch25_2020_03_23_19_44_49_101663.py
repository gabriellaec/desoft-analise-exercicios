import math
y=float(input("Velocidade:"))
x=float(input("Angulo:"))
x=math.radians(x)
d=(y**2*math.sin(2*x))/9.8
if d>=102:
    print('Muito longe')
elif d<=98:
    print('Muito perto')
else:
    print('Acertou!')