import math

def arcotangente(x, n):
    j = 3
    i=0
    soma = 0
    while i<n:
        while True:
            arctan = (x**j)/j
            soma = soma + arctan 
            i+=1
            j+=2
            break
        while True:
            arctan = (x**j)/j
            soma = soma-arctan 
            j+=2
            break
    soma = x-soma
    return soma