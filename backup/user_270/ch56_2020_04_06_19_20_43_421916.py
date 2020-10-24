import math
def calcula_norma(v):
    soma = 0
    for i in v:
        soma += i**2
    res = soma**(1/2)
    return res