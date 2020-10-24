import math

def arcotangente(x, n):
    j = 3
    i=0
    soma = x
    while i<n:
        while True:
            arctaneg = (x**j)/j
            soma = soma - arctaneg 
            i+=1
            j+=2
            break
        while True:
            arctan = (x**j)/j
            soma = soma+arctan
            i+=1
            j+=2
            break
    return soma