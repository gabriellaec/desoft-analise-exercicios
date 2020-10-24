import math
v = float(input('Qual a velocidade de lançamento?'))
theta = float(input('Qual o angulo de lançamento?'))
def jaca_wars(v,theta):
    d = ((v**2)* math.sin(math.radians(2*theta)))/9.8
    if d < 98:
        return 'Muito perto'
    elif d> 102:
        return 'Muito longe'
    else:
        return 'Acertou!'
print(jaca_wars(v,theta))