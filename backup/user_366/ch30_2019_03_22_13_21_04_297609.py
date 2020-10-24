import math

velo = float(input('Velocidade: '))
θ = float(input('Coloque o ângulo: '))

rad = θ*math.pi/180

dist = (math.sin(2*rad)*velo**2)/9.8

if dist == 100:
    print('Acertou!')
elif dist >= 98 and dist <= 102:
    print('Muito perto')
else:
    print('Muito longe')