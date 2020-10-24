import math
def calcula_euler(x,n):
    i = 0
    soma = 0
    while i < n:
        f = math.factorial(i)
        e = (x**i)/f
        soma += e
        i += 1
    return soma