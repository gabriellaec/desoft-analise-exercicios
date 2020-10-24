import math
def calcula_pi (n):
    i = 0
    resultado = 0
    while i < n:
        resultado += math.sqrt(6/i**2)
        i += 1
    return resultado
    