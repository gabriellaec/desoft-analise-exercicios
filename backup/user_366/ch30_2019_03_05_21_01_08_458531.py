import math

pede_velo = float(input('Qual a velocidade da jaca?'))
pede_ang = float(input('Qual o ângulo de lançamento?'))

c = math.sin(math.radians(2*θ))

def dist(pede_velo, c):
    y = pede_velo**2 * c / 9.8
    return y

y = dist(pede_velo, c)

if 98 < y < 102:
    print('Acertou!')
elif 96 < y or 102 < y < 104:
    print('Muito perto')
else:
    print('Muito longe')