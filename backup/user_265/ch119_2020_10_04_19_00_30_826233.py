import math 

def calcula_euler(x,n):
    soma = 1
    i = 1
        while i < n:
             soma += x**i/math.factorial(i) 
            i += 1

    return soma