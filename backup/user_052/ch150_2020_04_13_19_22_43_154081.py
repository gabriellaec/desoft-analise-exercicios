import math
def calcula_pi (n):
    i = 1
    resultado = 0
    while i <= n:
        resultado += 6/i**2
        i += 1
    return math.sqrt(resultado)
    