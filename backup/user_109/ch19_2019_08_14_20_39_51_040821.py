from math import sin, sqrt, radians


def calcula_distancia_do_projetil(v, y0, teta):

    tetaR = radians(teta)
    d = ((v**2)/(2*9.8))*(1 + (sqrt(1 + (2*9.8*y0)/((v**2)*(sin(tetaR))**2))) ) * (sin(2*tetaR))
    return d


v = float(input('Insira a velocidade do seu projétil: '))
y0 = float(input('Insira a altura inicial do seu projetil: '))
teta = float(input('Insira o ângulo de inclinação do seu lançador: '))

print(calcula_distancia_do_projetil(v, y0, teta))

