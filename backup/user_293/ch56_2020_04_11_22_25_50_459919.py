import math

def calcula_norma(vetor):
    soma = 0
    for e in vetor:
        d = e**2
        soma += d
    v = math.sqrt(soma)
    return v