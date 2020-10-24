from math import*
def calcula_euler(x, n):
    somatoria = 0
    resultado = 1 + x
    for n in range(2, n-1, 1):
        somatoria += (x**n)/(factorial(n))
        resultado += somatoria
    return resultado