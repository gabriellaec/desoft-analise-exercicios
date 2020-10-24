import math
def fatorial (n):
    i = 0 
    soma = 0 
    while i <= n:
        soma += math.factorial(i)
        i += 1
    return soma
