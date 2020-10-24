import math
def calcula_euler(x,n):
    i = 0
    soma = 0
    while i < n:
    e_x = x**n/math.factorial(n)
    soma += e_x
    i += 1
    return soma