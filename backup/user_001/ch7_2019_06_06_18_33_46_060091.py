import math
def calcula_norma(vetor):
    norma = 0
    for i in vetor:
        norma += math.fabs(i)
    return norma