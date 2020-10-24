from math import sin, sqrt


def lancador(v, y0, teta):
    d = (v**2/2*9.8)*(1 + sqrt(1 + (2*9.8*y0/(v**2)*(sin(teta)**2))))
    return d


v = float(input('Insira a velocidade do seu projétil: '))
y0 = float(input('Insira a altura inicila do seu projetil: '))
teta = float(input('Insira o ângulo de inclinação do swu lançador: '))

print(lancador(v, y0, teta))