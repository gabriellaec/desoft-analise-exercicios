import math

def arcotangente(x, n):
    j = 3
    i=1
    soma = x
    while i<n:
        if i%2!=0: 
            arctaneg = (x**j)/j
            soma = soma - arctaneg 
            i+=1
            j+=2
        else: 
            arctan = (x**j)/j
            soma = soma+arctan
            i+=1
            j+=2
    return soma