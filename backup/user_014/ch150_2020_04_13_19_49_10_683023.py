import math
def calcula_pi (n):
    i = 1
    soma = 0
    while n <=  1:
        soma = soma + (6/i**2)
        i += 1
    pi = math.sqrt(soma)
    return pi