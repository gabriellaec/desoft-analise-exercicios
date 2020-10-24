from math import sqrt
def calcula_pi(n):
    soma = 0
    i = 1
    while i < n:
        soma += sqrt(6/(i**2))
        i+=1
    return soma