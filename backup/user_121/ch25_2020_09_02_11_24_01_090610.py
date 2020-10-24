import math

velocidade = float(input('Qual a velocidade da jaca? '))
angulo = float(input('Ângulo de lançamento da jaca: '))

def acerto(v, a):
    g = 9.8
    d = v ** 2 * math.sin(math.radians(2 * a)) / g
    if d >= 98.0 and d <= 102.0:
        resultado = 'Acertou!'
    elif d < 98.0:
        resultado = 'Muito perto'
    else:
        resultado = 'Muito longe'
    return resultado

print(acerto(velocidade, angulo))