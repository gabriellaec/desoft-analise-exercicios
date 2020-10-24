from math import*
def calcula_euler(x, n):
    if n == 1:
        resultado = 1
    elif n == 2:
        resultado = 1 + x
    else:
        somatoria = 0
        resultado = 1 + x
        for n in range(2, n+1):
            somatoria += (x**n-1)/(factorial(n-1))
            resultado += somatoria
    return resultado