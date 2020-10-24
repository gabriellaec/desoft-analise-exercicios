import math

def arcotangente(x, n):
    j = 3
    i=0
    soma = 0
    while i<n:
        arctan = (x**j)/j
        soma = soma + arctan 
        i+=1
        j+=2
    soma = x-soma
    return math.radians(soma)
    