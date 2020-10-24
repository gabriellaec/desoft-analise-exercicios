import math
velocidade = float(input())
angulo = float(input())

d = ((velocidade**2)*math.sin(2*math.radians(angulo)))/9.8

if d<2:
    print('Muito perto')
elif d>4:
    print('Muito longe')
else:
    print("Acertou!")