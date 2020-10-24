from math import factorial
def calcula_euler(x,n):
    i = 0
    soma = 0
    while (i<n):
        soma = soma + (x**i)/(factorial(i))
        i += 1
    return soma
                              