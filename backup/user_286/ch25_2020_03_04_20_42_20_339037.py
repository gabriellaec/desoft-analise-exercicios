import math

velocidade = float(input('Qual a velocidade? '))
angulo = float(input('Qual o angulo? '))

sin = math.fabs(float(math.sin(2*angulo)))
dist = (velocidade**2)*(sin)/9.8

if dist < 98 or dist >102:
    print('Muito longe')
elif dist == 100:
    print('Acertou!')
else:
    print('Muito perto')