from math import fabs

def calcula_norma(vetor):
    soma = 0
    for e in vetor:
        soma += fabs(e)
    return soma