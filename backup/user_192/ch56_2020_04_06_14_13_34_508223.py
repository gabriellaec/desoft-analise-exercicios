import math
def calcula_norma(v):
    soma = 0
    for i in range (len(v)):
        soma += v**2
        modulo = math.sqrt(soma)
        soma += 1
    return modulo
    