from math import sqrt 
def calcula_pi(n):
    i = 0
    soma = 0
    while i <= n:
        conta = 6/(i**2)
        soma += conta
        i += 1
    pi = sqrt(soma)
    return pi 
