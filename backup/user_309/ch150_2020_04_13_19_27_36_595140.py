from math import sqrt 
def calcula_pi(n):
    i = 0
    soma = 0
    while i <= n:
        conta = 6/n**2
        soma += conta
        pi = sqrt(soma)
        n += 1
    return pi 
