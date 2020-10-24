import math
velocidade = float(input('Insira a velociadade no lançamento '))
angulo = float(input('Insira o ângulo de lançamento '))
def testa_se_acertou(velocidade, angulo):
    g = 9.8
    d = (velocidade**2*math.sin(math.pi*angulo/90))/g
    if d<102 and d>98:
        print('Acertou!')
        return d
    elif d>102:
        print('Muito longe')
        return d
    else:
        print('Muito perto')
        return d
testa_se_acertou(velocidade, angulo)