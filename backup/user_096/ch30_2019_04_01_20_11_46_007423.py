import math 
v = float(input('qual a velocidade: '))
o = float(input('qual o angulo: '))
distancia = ((v**2)*math.sin(2*math.radians(o)))/9.8
if distancia > 102:
    print('Muito longe')
elif distancia < 98:
    print('Muito perto')
elif 98<=distancia<=102:
    print('Acertou!')


