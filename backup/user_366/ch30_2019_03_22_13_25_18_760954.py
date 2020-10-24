import math

velo = float(input('Velocidade: '))
θ = float(input('Coloque o ângulo: '))

rad = θ*math.pi/180

dist = (math.sin(2*rad)*velo**2)/9.8

if dist > 102:
    print('Muito longe')
elif dist < 98:
    print('Muito perto')
else:
    print('Acertou!')