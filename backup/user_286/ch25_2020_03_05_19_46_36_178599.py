import math

velocidade = int(input('Qual a velocidade? '))
angulo = int(input('Qual o angulo? '))

radian = angulo*math.pi/180

sin = float(math.sin(2*radian))
dist = (velocidade**2)*(sin)/9.8

if dist < 98:
    print('Muito perto')
elif dist >= 98 or dist <= 102:
    print('Acertou!')
else:
    print('Muito longe')
