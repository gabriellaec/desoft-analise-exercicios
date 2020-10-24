import math
velocidade=float(input('Qual é a velocidade?:'))
angulo=float(input('Digite o angulo:'))
d=((velocidade**2)*math.sin(2*math.radians(angulo)))/9.8
if d<98:
    print('Muito perto')
elif d>102:
    print('Muito longe')
else:
    print('Acertou!')