from math import factorial
def calcula_euler(x,n):
    i = 0
    soma = 0
    while (i+1<n):
        soma = soma + (x**n)/(factorial(n))
        i += 1
    return soma
                              