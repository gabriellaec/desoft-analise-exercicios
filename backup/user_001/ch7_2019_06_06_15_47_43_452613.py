import math
def calcula_norma(vetor):
    i = 0
    t = 0
    s = 0
    while i<len(vetor):
        t = vetor[i]**2
        s += t
        i += 1
    v = math.sqrt(s)
    return v