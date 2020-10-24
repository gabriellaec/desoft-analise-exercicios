import math
x = float(input('Qual a velocidade e de lançamento da jacosa?'))
y = float(input('Qual o ângulo de lançamento da jacosa?'))
def distancia_da_jaca(v, θ):
    h = (180 / math.pi) *  θ
    d = (v**2 * math.sin(2*h)) / 9.8
    if d < 98:
        return 'Muito perto'
    elif d > 102:
        return 'Muito longe'
    else:
        return 'Acertou!'

print(distancia_da_jaca(x, y))

