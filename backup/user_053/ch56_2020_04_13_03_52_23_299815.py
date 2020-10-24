import math

def calcula_norma(vetor):
    if len(vetor) == 1:
        norma = vetor[0]
    else:
        norma = math.sqrt((vetor[0])**2 + (vetor[len(vetor) - 1])**2)
    return norma