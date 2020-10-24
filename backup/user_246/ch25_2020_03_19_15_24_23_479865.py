import math
x=int(input("Angulo:"))
y=int(input("Velocidade:"))
d=(y**2*math.sin(2*x))/9.8
if d>100:
    print('Muito longe')
elif d<100:
    print('Muito perto')
else:
    print('Acertou!')