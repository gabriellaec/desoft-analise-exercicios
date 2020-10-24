import math
def calcula_norma(vetores):
    v = 0
    for i in vetores:
        v += i**2
    V = math.sqrt(v)
    return V