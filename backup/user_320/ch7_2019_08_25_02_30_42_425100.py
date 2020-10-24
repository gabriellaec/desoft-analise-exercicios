from math import sqrt
def calcula_norma(vetor):
    n = 0
    for elemento in vetor:
        n += elemento ** 2
    norma = sqrt(n)
    return norma