import math

def calcula_norma(vetor):
    soma = 0
    for e in vetor:
        soma+=e**2
    return math.sqrt(soma)
