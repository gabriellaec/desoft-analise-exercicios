import math
def calcula_norma(vetor):
    i = 0
    t = 0
    s = 0
    while i<len(vetor):
        t = math.fabs(vetor[i])
        s += t
        i += 1
    return s