import math
def calcula_norma(vetor):
    parcelas=[]
    for i in vetor:
        parcelas.append(i**2)
    return math.sqrt(sum(parcelas))