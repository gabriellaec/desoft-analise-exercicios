import math
def calcula_pi (n):
    i = 1
    soma = 0
    while n <=  i:
        soma = soma + (6/i**2)
        i += 1
    pi = math.sqrt(soma)
    return pi