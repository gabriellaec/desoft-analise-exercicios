from math import sin
vel = float(input('Digite a velocidade da jaca: '))
teta = float(input('Digite o angulo de lançamento de sua jaca: '))
g = 9.8
dist = ((vel**2)*sin(2*teta))/g


if dist > 98:
    print('Muito perto')
elif dist > 102:
    print('Muito longe')
else:
    print('Acertou!')
    
