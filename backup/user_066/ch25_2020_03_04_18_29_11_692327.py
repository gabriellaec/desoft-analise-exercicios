import math
velocidade = int(input('Insira a velociadade no lançamento '))
angulo = int(input('Insira o ângulo de lançamento '))
def testa_se_acertou(velocidade, angulo):
    d = velocidade**2*math.sin(math.pi*angulo/90)
    if d<110 and d>90:
        print('Acertou!')
        return "acertou"
    elif d>110:
        print('Muito longe')
        return "Errou"
    else:
        print('Muito perto')
        return "Errou"
testa_se_acertou(velocidade, angulo)