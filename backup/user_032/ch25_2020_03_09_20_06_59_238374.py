import math
v = int(input('Qual a velocidade de lançamento?'))
θ = int(input('Qual o angulo de lançamento?'))
def jaca_wars(v,θ):
    d = ((v**2)* math.sin(2*θ))/9.8
    if d <= 98:
        print('Muito perto')
    elif d>= 102:
        print('Muito longe')
    else:
        print('Acertou!')