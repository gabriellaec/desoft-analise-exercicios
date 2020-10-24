import math
def jaca_wars(v,θ):
    v=int(input('Qual a velocidade da jaca? '))
    θrad=int(input('Qual o ângulo do lançamento(em rad)? '))
    θrad=(θ*math.pi)/180
    d=((v**2)*math.sin(2*θ))/9.8
    if d<98:
        print('Muito perto')
    elif d>102:
        print('Muito longe')
    else:
        print('Acertou!')
    return d
    