import math

pede_velo = float(input('Qual a velocidade da jaca?'));
pede_ang = float(input('Qual o ângulo de lancamento?'));

math.radians(pede_ang);

def dist(v, θ):
    y = v**2 * math.sin(2*θ) / 9.8
    return y

v = pede_velo
θ = pede_ang
y = dist(v, θ)

if 98 <= y <= 102:
    print('Acertou!');
elif 90 < y:
    print('Muito perto');
else:
    print('Muito longe');