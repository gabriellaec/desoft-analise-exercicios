import math

pede_velo = float(input('Qual a velocidade da jaca?'));
pede_ang = float(input('Qual o ângulo de lancamento?'));

v = pede_velo
θ = pede_ang
c = math.sin(math.radians(2*θ))

def dist(v, θ):
    y = v**2 * c / 9.8
    return y

y = dist(v, c)

if 98 <= y <= 102:
    print('Acertou!');
elif 90 < y or 102 < y < 110:
    print('Muito perto');
else:
    print('Muito longe');