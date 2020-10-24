from math import sin, radians

def distancia(v, angulo):
    y = (v**2)*sin*(radians(2*angulo))/9.8
    return y

v = input('Qual é a velocidade? ')
angulo = input('Qual é o angulo de lançamento da jaca? ')

if distancia(v, angulo) < 98:
    print('Muito perto')
elif distancia(v, angulo) > 102:
    print('Muito longe')
else:
    print('Acertou!')