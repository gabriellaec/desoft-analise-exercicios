import math
def calcula_norma(lista):
    for comprimento in lista:
        comprimento += comprimento**2
    modulo = math.sqrt(comprimento)
    return modulo