from math import*
def calcula_euler(x, n):
    somatoria = 0
    for n in range(2, n-1, 1):
        somatoria += (x**2)/(factorial(n))
    resultado = 1 + x + somatoria
    return resultado