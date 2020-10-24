import math
def calcula_pi(n):
    c = n
    soma = 0
    while (c != 0):
        soma += 6/c**2
        c = c - 1
    pi = math.sqrt(soma)
    return pi