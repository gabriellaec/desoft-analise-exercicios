from math import*
def calcula_euler(x, n):
    if n == 1:
        resultado = 1
    elif n == 2:
        resultado = 1 + x
    else:
        somatoria = 0
        resultado = 1 + x
        for elemento in range(3, n+1):
            somatoria += (x**elemento-1)/(factorial(elemento-1))
        resultado += somatoria
    return resultado