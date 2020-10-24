from math import sqrt 
def calcula_pi(n):
    n = 1
    soma = 0
    while n != 0:
        conta = 6/n**2
        soma += conta
        pi = sqrt(soma)
        n += 1
    