import math

def arcotangente(x, n):
    j = 3
    i=1
    soma = 0
    while i<n:
        arctan = (x**j)/j
        soma = soma + arctan 
        i+=1
        j+=2
    soma = x-soma
    return soma
    