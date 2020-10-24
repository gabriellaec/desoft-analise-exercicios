import math

velocidade = float(input('Qual a velocidade? '))
angulo = float(input('Qual o angulo? '))

dist = (velocidade**2(math.sin(2*angulo)))/9.8

if dist < 98 or dist >102:
    print('Muito longe')
elif dist == 100:
    print('Acertou!')
else:
    print('Muito perto')