import math
def calcula_norma(vetor):
    vetores_2 =[]
    for i in vetor:
        vetores_2.append(i**2)
    s = sum(vetores_2)
    r = math.sqrt(s)
    return r