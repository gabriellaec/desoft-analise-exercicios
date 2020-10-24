import math
v = int(input('Qual a velocidade de lançamento?'))
theta = int(input('Qual o angulo de lançamento?'))
def jaca_wars(v,theta):
    d = ((v**2)* math.sin(math.radians(2*theta)))/9.8
    if d <= 98:
        print('Muito perto')
    elif d>= 102:
        print('Muito longe')
    else:
        print('Acertou!')